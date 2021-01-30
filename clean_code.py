# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:41:50 2020 @author: plouk
τα στάδια αυτής της μεθοδολογίας είναι τα παρακάτω
# ===================== 1. Region-based background segmentation ============================
# ===================== 2. Body-Tissue Clustering Stage ====================================
# ===================== 3. BAT/WAT ROI ανίχνευση με density-based παράθυρο =================
keywords: subcutaneous -- υποδόριος/υποδερμικό
          intrascapular -- δια-ωμοπλατιαίος
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage.util import img_as_ubyte
from skimage.restoration import estimate_sigma, denoise_wavelet
from skimage.filters import sobel, unsharp_mask
from skimage.exposure import histogram
from skimage.segmentation import watershed
from skimage.segmentation import random_walker
from skimage.measure import regionprops
from skimage.transform import downscale_local_mean
from skimage.draw import rectangle, rectangle_perimeter, circle, circle_perimeter
from skimage.filters.rank import entropy
from skimage.morphology import disk, skeletonize, thin
from skimage.feature import hog
from skimage.feature import (greycomatrix, greycoprops,
                             local_binary_pattern, multiblock_lbp, draw_multiblock_lbp)

from sklearn.feature_extraction import img_to_graph, grid_to_graph
from sklearn import cluster
from sklearn import preprocessing
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from scipy import ndimage as ndi

from load_images import load_images
from readable_EXIF import readable_EXIF
from img_to_vectors import img_to_vectors
from load_csv import load_csv

# Επεξεργασία του ποντικιού Άκης, επιλέγοντας τις καλύτερες —κατ'εμέ— εικόνες
# Ποντίκια Άκης Γάκης Δάκης Λάκης Μάκης
# basically we are building a data frame with all the columns made into a feature vector
# and the rows are going to be samples of the experiment
sampleHours = ['0h', '24h', '48h', '72h', '96h', '120h', '144h', '192h', '240h']
# import image sequence with immediate grayscale conversion
# η αρχική ανάλυση της εικόνας είναι (240, 320)
rawImages, rawEXIF = load_images(name='BAT')
# sensorData = load_csv(sampleHours, name='BAT')
# [readable_EXIF(rawdata) for rawdata in rawEXIF]

# Display purposes: clear the FLIR logo and the pseudo-color scale
# με το κεντράρισμα του ποντικιού ρίχνουμε το μέγεθος σε (240, 144)
cutImages = [mouseImage[:, 100:260] for mouseImage in rawImages]

# for cutImage, rawImage in zip(cutImages, rawImages):
#     #-------------- Figure: 2-figure considered with the background/object segmentation --------
#     fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
#     fig.suptitle('Border Removal')
#     axs[0].imshow(rawImage, cmap=plt.cm.nipy_spectral)
#     axs[0].axvline(x=100, c='red')
#     axs[0].axvline(x=260, c='red')
#     axs[1].imshow(cutImage, cmap=plt.cm.nipy_spectral)

# στατιστικά εικόνας, πριν κάνουμε αλλαγές
# sigmaEstimatesBefore = [estimate_sigma(mouseImage) for mouseImage in cutImages]
# meanBefore = [np.mean(mouseImage) for mouseImage in cutImages]
# SNRBefore = list(map(lambda x, y: x / y, meanBefore, sigmaEstimatesBefore))

# downscale + unsharp mask when using a graph-based method due to memory complexity
# εδώ προφανώς θα πέσουμε στα (120, 77)
# preprocessing // αλλαγές: αποκλιμάκωση εικόνας και αφαίρεση θορύβου
mouseImages = [downscale_local_mean(mouseImage, (2, 2)) for mouseImage in cutImages]
# or denoise_wavelet
mouseImages = [unsharp_mask(mouseImage) for mouseImage in mouseImages]

# # στατιστικά εικόνας, αφού κάνουμε αλλαγές
# sigmaEstimatesAfter = [estimate_sigma(mouseImage) for mouseImage in mouseImages]
# meanAfter = [np.mean(mouseImage) for mouseImage in mouseImages]
# SNRAfter = list(map(lambda x, y: x / y, meanAfter, sigmaEstimatesAfter))


# fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))
# fig.suptitle('Estimated SNR')
# axs.plot(np.arange(9), SNRBefore, 'k--', label='Raw Image')
# axs.scatter(np.arange(9), SNRBefore, s=5, c='black')
# axs.plot(np.arange(9), SNRAfter, 'k', label='Downscale + Denoise')
# axs.scatter(np.arange(9), SNRAfter, s=5, c='black')
# legend = axs.legend(loc='best', fontsize='x-large')


markerBack, markerBody = 70, 150
n_clusters = 6
n_features = 2
np.random.seed(0)
# για το αρχικό clustering.Kmeans() iteration, στη συνέχεια αλλάζει τύπο και γίνεται τα κεντροειδή
CENTROIDS = 'k-means++'
# για την παράμετρο της μεθόδου της υφής
METHOD = ('uniform', 'default', 'ror', 'var')
clusteringScores = []

for cutImage, sampleHour in zip(mouseImages, sampleHours):
    print('=============== sample of ==================', sampleHour)
    # ===================== 1. Region-based background segmentation ============================
    # this mask is going to be topologically processed for the tissue segmentation
    # either the BAT which is close to the back neck, or WAT which is close to the belly
    # Κάνουμε μια region-based μέθοδο χρησιμοποιώντας την κατάτμηση watershed για μια binary μάσκα.

    #-------------- Figure: 2-figure considered with the background/object segmentation --------
    hist, hist_centers = histogram(img_as_ubyte(cutImage))
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
    fig.suptitle('Histogram prior to detection')
    axs[0].imshow(cutImage)
    axs[1].plot(hist_centers, hist, lw=1)
    # axs[1].axvline(backgroundMarker, color='r', linestyle='--')
    # axs[1].axvline(bodyMarker, color='b')
    # axs[1].set_title(sampleHour + ' histogram')

    # We create markers indicating the segmentation through histogram values
    mouseMarker = np.zeros_like(cutImage)

    # We find markers of the background and the mouse body based on the extreme
    # parts of the histogram of gray values.
    # μαρκάρω == marker, πινακιδιάζω == label

    mouseMarker[img_as_ubyte(cutImage) < markerBack] = 1
    mouseMarker[img_as_ubyte(cutImage) > markerBody] = 2
    # We use the watershed transform to fill regions of the elevation
    # map starting from the markers determined above
    # find an elevation map using the image Sobel gradient.
    elevationMap = sobel(cutImage)
    initialMask = watershed(elevationMap, mouseMarker)

    # This method segments and labels the mouse individually
    initialMask = ndi.binary_fill_holes(initialMask - 1)

    labeledMouse, _ = ndi.label(initialMask)

    # βρήκαμε ένα αντικείμενο -ωραία
    # επιστρέφει έναν τύπο δεδομένων, που λέγεται slice, ένα τετράγωνο μέσα στην αρχική εικόνα
    # είναι σαν generator range object, με διάφορα attributes / methods
    mouseLocation = ndi.find_objects(labeledMouse)[0]

    # Μειώνουμε και άλλο την εικονα στο ακριβες κουτι του ποντικιου
    mouseImage = cutImage[mouseLocation]
    mouseMask = initialMask[mouseLocation]

    # μάσκα ποντικιού και ανάλυση σε διανύσματα συντεταγμένων
    maskOrdinateX, maskOrdinateY = img_to_vectors(mouseMask)
    n_samples = maskOrdinateX.size # == maskOrdinateY.size φυσικά


    #-------------- Figure: 2-figure considered with the background/object segmentation --------
    hist, hist_centers = histogram(img_as_ubyte(mouseImage))
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))
    fig.suptitle('Histogram post detection')
    axs[0].imshow(mouseImage, cmap=plt.cm.nipy_spectral)
    axs[0].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[1].imshow(entropy(img_as_ubyte(mouseImage), disk(5)), cmap=plt.cm.nipy_spectral)
    axs[1].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[2].plot(hist_centers, hist, lw=1)

    # γεωμετρικά χαρακτηριστικά της μάσκας και του τόπου αναζήτησης στο ποντίκι
    # σκελετός και χώρος αναζήτησης region of interest
    maskInfo = regionprops(mouseMask.astype('int'), mouseImage)
    # maskInfo = regionprops(mouseMask.astype('int'))
    # print('translation vector: ', translationVector.ravel())
    # translationVector = np.array([maskInfo[0].centroid[1], maskInfo[0].centroid[0]]).T - translationVector

    # σκελετός και ανάλυση σε διανύσματα συντεταγμένων του
    skeletonImage = skeletonize(mouseMask)
    skeletonOrdinateX, skeletonOrdinateY = img_to_vectors(skeletonImage)

    # εκλέπτυνση και ανάλυση σε διανύσματα συντεταγμένων του
    thinImage = thin(mouseMask)
    thinOrdinateX, thinOrdinateY = img_to_vectors(thinImage)

    # ανίχνευση με κατασκευή παράθυρου, όπου θα φτίαξουμε το εμβαδόν του
    # inter-scapular =  δια-ωμοπλατιαίος
    # πού είν' τ'αυτιά; -εκεί είναι τα όρια της ωμοπλάτης, κάτω από τη μέση
    # σε ένα σημείο το οριζόντιο μήκος πέφτει, άρα υπολογίζουμε τα οριζόντια μήκη για αρχή από τη μάσκα

    # print(sum(mouseMask, axis=0))

    #-------------- Figure: 5-figure 1. elevation map 2. markers 3. mask 4. skeleton 5. thin --------
    fig, axs = plt.subplots(nrows=1, ncols=5, figsize=(8, 4))
    fig.suptitle(sampleHour + 'samples/mouseArea')
    axs[0].imshow(elevationMap, cmap=plt.cm.gray)
    # axs[0].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[0].set_title('Elevation Map')
    axs[1].imshow(mouseMarker, cmap=plt.cm.gray)
    axs[1].set_title('Hist. Markers')
    axs[2].imshow(mouseMask, cmap=plt.cm.gray)
    axs[2].scatter(x=maskInfo[0].centroid[1], y=maskInfo[0].centroid[0], c='red', s=3)
    axs[2].set_title('Mask')
    axs[3].imshow(skeletonImage, cmap=plt.cm.gray)
    axs[3].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[3].set_title('Skeleton')
    axs[4].imshow(thinImage, cmap=plt.cm.gray)
    axs[4].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[4].set_title('Thining')


    #-------------- Figure: 2-figure of the segmented object values ----------------------------
    # fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 4), sharey=True)
    # fig.suptitle(sampleHour + ' borders')
    # axs[0].imshow(mouseImage, cmap=plt.cm.nipy_spectral)
    # axs[0].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # axs[0].set_title('original image')
    # #mouseMask[mouseLocation] = True
    # axs[1].imshow(label2rgb(labeledMouse, image=mouseImage, bg_label=0))
    # axs[1].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # axs[1].set_title('segmented mouse')

    # ===================== 2. Body-Tissue Clustering Stage ========================================
    #-------------- Creating / Selecting clustering Features  ----------------------------
    # todo: find more features to cluster, like the image texture

    # κατασκευή του διανύσματος feature για τον αλγόριθμο συσταδοποίησης
    # mouse intensity made into a vector of length {n_samples}
    intensityFeature = np.zeros(n_samples, dtype='float64')
    # mouseImage_ubyte = img_as_ubyte(mouseImage)
    for i in range(n_samples):
        intensityFeature[i] = mouseImage[maskOrdinateX[i], maskOrdinateY[i]]

    # segmentedImage: εικόνα διάστασης mouseImage με μαύρο background
    segmentedImage = np.zeros_like(mouseImage)
    for i in range(n_samples):
        segmentedImage[maskOrdinateX[i]][maskOrdinateY[i]] = intensityFeature[i]

    #-------------- Figure: 2-figure considered with the background/object segmentation --------
    hist, hist_centers = np.histogram(intensityFeature, bins=256, range=(0,255))
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
    # fig.subtitle('Tissue Histogram')
    axs[0].imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    axs[0].contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    axs[1].plot(hist_centers[1:], hist, lw=1)

    # δοκιμαζω το hog 
    hog_vec, hog_vis = hog(segmentedImage, visualize=True)

    # βγάζω την εικόνα texture για να την περάσω ως feature προς τη μέθοδο συσταδοποίησης
    radius = 10
    n_points = 8 * radius + 4
    textureImage = local_binary_pattern(image=segmentedImage, P=n_points, R=radius, method=METHOD[0])
    # textureImage = textureImage.astype('int')
    # textureImage = img_as_float(textureImage)

    # mouse texture made into a vector of length {n_samples}
    textureFeature = np.zeros(n_samples)
    for i in range(n_samples):
        textureFeature[i] = textureImage[maskOrdinateX[i], maskOrdinateY[i]]

    # το αντίστροφο να φτιάξουμε μια εικόνα μέσω της μάσκας
    segmentedTexture = np.zeros_like(segmentedImage)
    for i in range(n_samples):
        segmentedTexture[maskOrdinateX[i]][maskOrdinateY[i]] = textureFeature[i]

    #-------------- Figure: 2-figure considered with the background/object segmentation --------
    # textureFeature, bins=np.max(textureFeature), range=(0,255)
    hist, hist_centers = np.histogram(segmentedTexture)
    # hist, hist_centers = histogram(textureImage)
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))
    # fig.subtitle('Texture of segmented image')
    # axs[0].imshow(segmentedTexture, cmap=plt.cm.nipy_spectral)
    axs[0].imshow(hog_vis)
    axs[1].plot(hist_centers[1:], hist, lw=1)
    # axs[1].axvline(markerBack, color='r', linestyle='--')
    # axs[1].axvline(markerBody, color='b')
    axs[1].set_title('segmented Texture')

    #-------------- Figure: 2-figure the used features: intensity and texture ----------------------------
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
    fig.suptitle('Utilized Features' + sampleHour)
    axs[0].imshow(X=segmentedImage, cmap=plt.cm.nipy_spectral)
    axs[0].set_title('Intensity')

    axs[1].imshow(textureImage, cmap=plt.cm.gray)
    axs[1].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    axs[1].set_title('Texture, Skeleton')

    axs[2].imshow(textureImage, cmap=plt.cm.gray)
    axs[2].scatter(x=thinOrdinateY, y=thinOrdinateX, c='red', s=1)
    axs[2].set_title('Texture, Thin')

    # ------------------ Building the feature vector X{n_samples, n_features} ----------------------
    # Σε αυτό το σημείο θα μπορούσαμε να κάνουμε feature extraction μέσα από την εικόνα
    # => βιβλιοθήκη skimage.transform και να το προσθέσουμε στο διάνυσμα Χ
    # constructing sample-feature vector X {n_samples, n_feature}
    # clustering features => X{n_samples, n_features}
    # if n_features = 3 (if no other transformation is done)
    # x, y : mouse coordinates and f(x, y) mouse-body intensity
    # n_samples => X.shape[0] is equal to the mouse area

    # first stack (maskOrdinateX.ravel(), maskOrdinateY.ravel(), intensityFeature)
    X = np.vstack((textureFeature, intensityFeature))
    # X = intensityFeature.reshape(-1, 1)
    # αν κανουμε clustering με το intensity ως feature
    # δηλαδή np.vstack((intensityFeature)) => (n_feature = 1)
    # τότε να κάνεις σχόλιο την παρακάτω γραμμή γιατί αλλιώς μπερδεύει τις διαστάσεις του Χ
    X = X.transpose()
    # #--------------- 2a Feature Scaling Methods ---------------------------------
    # scaler = preprocessing.MinMaxScaler()
    scaler = preprocessing.RobustScaler()
    # #scaler = preprocessing.MaxAbsScaler()
    # #scaler = preprocessing.Normalizer()
    # # scaler = preprocessing.StandardScaler()
    X = scaler.fit_transform(X)
    # # tweaking the hyperparameter
    lamdaHyperparameter = 20.0
    #X[:, 1] = np.sqrt(lamdaHyperparameter) * X[:, 1]

    #------------------- 2. Clustering Methods ----------------------------------
    #------------------- Distanced based: Kmeans --------------------------------
    kMeans = cluster.KMeans(n_clusters=n_clusters, init=CENTROIDS)
    kMeans.fit(X)
    CENTROIDS = kMeans.cluster_centers_.squeeze() # no random init at next iteration
    # print('Distance-based mouse centroids are ', CENTROIDS)
    labels = kMeans.labels_

    # #------------------- Density based: Mean Shift ----------------------
    # meanShift = cluster.MeanShift()
    # meanShift.fit(X)
    # CENTROIDS = meanShift.cluster_centers_.squeeze()
    # # print('Density-based mouse centroids are ', CENTROIDS)
    # labels = meanShift.labels_
    #------------------- Density based: DBSCAN ------------------------
    # eps: μεγιστη απόσταση για να θεωρήσουμε το ένα γειτονιά του αλλου
    # dbscan = cluster.DBSCAN(eps=0.2, min_samples=9, leaf_size=8)
    # labels = dbscan.fit_predict(X)

    #------------------- Density based: OPTICS ------------------------
    # optics = cluster.OPTICS(min_samples=9, max_eps=0.2, xi=.05, min_cluster_size=200)
    # labels = optics.fit_predict(X)

    #------------------- Graph based: Spectral clustering --------------
    # spectral = cluster.SpectralClustering(n_clusters=n_clusters, affinity='nearest_neighbors', \
    #                                       n_neighbors=8, assign_labels='kmeans')
    # spectral.fit(X)
    # # ομοιότητα : affinity  είναι ένας similarity πίνακας, με όλους τους συνδυασμούς των δειγμάτων
    # affinity = spectral.affinity_matrix_.toarray()
    # labels = spectral.labels_

    #------------------- 2b Metrics: Internal cluster evaluation  -----------
    score = (silhouette_score(X, labels),
             calinski_harabasz_score(X, labels),
             davies_bouldin_score(X, labels))
    clusteringScores.append(score)
    # print('For n_clusters =', n_clusters,
    #       '\n Average Silhouette Score:', scoreSilhouette,
    #       '\n Variance Ratio Criterion:', scoreVarianceRatio,
    #       '\n Within to between-cluster:', scoreDavies)

    # original-sized image, with the labels + 1 given by the clustering algorithms
    labeledImage = np.zeros_like(mouseImage, dtype='int')
    for i in range(n_samples):
        labeledImage[maskOrdinateX[i]][maskOrdinateY[i]] = labels[i] + 1

    # η παρακάτω λίστα είναι σε μήκος όση και τα n_cluster (== label number),
    # δίνει πληροφορίες για κάθε περιοχή όσον αφορά σε σχήματα από κουτιά,
    # ειδικά για τις συντεταγμένες τους, τα εμβαδά τους και τα μήκη των καμπυλών
    clustersInfo = regionprops(labeledImage, segmentedImage)

    # λίστα από δι-tuples με μήκος n_clusters πχ [(80, 12), (40, 13)]
    # γενικά: info_list = [info.attribute for info in clustersInfo]
    clusterCentroids = [clusterElement.centroid for clusterElement in clustersInfo]
    # θα τα κανω scatter plot οπότε σημαίνει δύο λίστες x = [80, 40] y = [12, 13]
    # άρα τα κάνω unpack με το
    centroidRow, centroidColumn = map(list, zip(*clusterCentroids))

    #-------------- Figure: 2-figure of the segmented object values ----------------------------
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
    fig.suptitle(sampleHour)
    axs[0].imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    axs[0].set_title('segmented mouse')
    axs[0].scatter(x=centroidColumn, y=centroidRow, c='white', s=6)
    # label2rgb(label=labeledImage, image=segmentedImage, bg_label=0, alpha=0.5)
    axs[1].imshow(labeledImage, cmap=plt.cm.nipy_spectral)
    axs[1].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    axs[1].set_title('clustering + skeleton')
    # label2rgb(label=labeledImage, image=segmentedImage, bg_label=0, alpha=0.5)
    axs[2].imshow(labeledImage, cmap=plt.cm.nipy_spectral)
    axs[2].scatter(x=thinOrdinateY, y=thinOrdinateX, c='white', s=1)
    axs[2].set_title('clustering + thin')

    #================= 3 BAT extraction from the ROI ===============================

    # ROI contains multiple labels, how do we deal with the exact roi location?
    # θα κανουμε μια προσεγγιση με το σκελετο ως ραγα για τις περιοχές όπου θα
    # περάσει το παραθυρο αναζητησης
    # το παραθυρο αναζητησης εχει ενα σχημα και συγκεντρωνει τα labels φτιαχνοντας ενα ιστογραμμα
    # σειριακα συγκρινουμε τα ιστογραμματα ως πυκνοτητα πιθανοτητας και βρισκουμε την εντροπια
    # ή την κοινη πληροφορια τους ως μέτρο σφαλματος
    # μεχρι να μην ξεπερασουμε τα γεωμετρικά όρια του αυχένα / ωμοπλάτης
    sample = 70
    r, c = skeletonOrdinateX[sample], skeletonOrdinateY[sample]
    # rr, cc = rectangle(start=(r, c), extent=(-10, 10), shape=mouseImage.shape)

    # maskBAT = np.zeros_like(segmentedImage)
    # maskBAT[rr, cc] = 1
    # tissueBAT = segmentedImage * maskBAT

    # fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    # fig.suptitle(sampleHour)
    # axs[0].imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    # axs[0].contour(maskBAT)
    # axs[0].set_title('Seed points')
    # axs[0].scatter(x=centroidColumn, y=centroidRow, c='white', s=6)
    # axs[1].imshow(tissueBAT, cmap=plt.cm.gray)
    # axs[1].set_title('Seed image')

    centroidColumn, centroidRow = list(map(int, centroidColumn)), list(map(int, centroidRow))
    # filter()
    seedImage = np.zeros_like(segmentedImage)

    # seedImage[centroidRow[1]:centroidRow[1] + 6, centroidColumn[1]:centroidColumn[1] + 6] = 2
    # seedImage[centroidRow[2]:centroidRow[2] + 6, centroidColumn[2]:centroidColumn[2] + 6] = 1

    # seedImage[skeletonOrdinateX[slice(None, skeletonOrdinateX.size // 4)], skeletonOrdinateY[slice(None, skeletonOrdinateY.size // 4)]] = 2
    # seedImage[thinImage] = 1
    # άμα έχει μέχρι δύο label τότε επιστρέφει για κάθε ένα ξεχωριστό πίνακα με το return_full_prob=True

    # rrr1, ccc1 = rectangle_perimeter(start=(r, c), extent=(-10, -10), shape=seedImage.shape)
    rrr1, ccc1 = circle_perimeter(r, c, radius=9, shape=seedImage.shape)
    seedImage[rrr1, ccc1] = 1
    # rrr2, ccc2 = rectangle_perimeter(start=(r, c), extent=(-15, -15), shape=seedImage.shape)
    rrr2, ccc2 = circle_perimeter(r, c, radius=5, shape=seedImage.shape)
    seedImage[rrr2, ccc2] = 2

    # Δοκιμές με τι δεδομένα να κάνουμε την αποκοπή
    outputIntensity = random_walker(data=segmentedImage, labels=seedImage, beta=80, return_full_prob=False)
    outputTexture = random_walker(data=textureImage, labels=seedImage, beta=80, return_full_prob=False)
    outputLabeled = random_walker(data=segmentedImage, labels=labeledImage, beta=80, return_full_prob=False)
    #-------------- Figure: 3-figure of seed points, seed image and result ----------------------------
    fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(8, 4))
    fig.suptitle(sampleHour)
    axs[0].imshow(labeledImage, cmap=plt.cm.nipy_spectral)
    axs[0].set_title('MouseImage')
    axs[0].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    axs[1].imshow(outputLabeled, cmap=plt.cm.nipy_spectral)
    # axs[1].contour(outputImage)
    # axs[1].scatter(x=c, y=r, c='white', s=16)
    # axs[1].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    axs[1].set_title('BAT labeled')
    axs[2].imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    axs[2].contour(outputIntensity, [0.5], linewidths=1.2, colors='w')
    axs[2].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    axs[2].set_title('BAT intensity')
    axs[3].imshow(textureImage, cmap=plt.cm.gray)
    axs[3].contour(outputTexture, [0.5], linewidths=1.2, colors='w')
    axs[3].scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    axs[3].set_title('BAT texture')

# λίστα από 3-tuples με μήκος n_clusters πχ [(80, 12, 16), (40, 13, 17)]
# allScores = [score for score in clusteringScores]
# θα τα κανω scatter plot οπότε σημαίνει 3 λίστες
# x = [80, 40] y = [12, 13] z = [16, 17] άρα τα κάνω unpack με το
silhouette, calinski, davies = map(list, zip(*clusteringScores))
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))
axs[0].plot(np.arange(9), silhouette, 'k--', label='Raw Image')
axs[1].plot(np.arange(9), calinski, 'k--', label='Raw Image')
axs[2].plot(np.arange(9), davies, 'k--', label='Raw Image')
