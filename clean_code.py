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
print(__doc__)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from skimage.util import img_as_ubyte
from skimage.restoration import estimate_sigma, denoise_wavelet
from skimage.filters import sobel, unsharp_mask
from skimage.exposure import histogram
from skimage.segmentation import watershed
from skimage.segmentation import random_walker
from skimage.measure import regionprops, regionprops_table, find_contours
from skimage.transform import downscale_local_mean
from skimage.draw import rectangle, rectangle_perimeter, circle, circle_perimeter
from skimage.filters.rank import entropy
from skimage.morphology import disk, square, skeletonize, thin, dilation
from skimage.feature import greycomatrix, greycoprops, local_binary_pattern

from sklearn.feature_extraction import img_to_graph, grid_to_graph
from sklearn import cluster
from sklearn import preprocessing
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from scipy import ndimage as ndi

from load_images import load_images
from img_to_vectors import img_to_vectors
from load_csv import load_csv
from gif_maker import gif_maker
# Επεξεργασία του ποντικιού Άκης, επιλέγοντας τις καλύτερες —κατ'εμέ— εικόνες
# Ποντίκια Άκης Γάκης Δάκης Λάκης Μάκης
# basically we are building a data frame with all the columns made into a feature vector
# and the rows are going to be samples of the experiment
sampleHours = ['0h', '24h', '48h', '72h', '96h', '120h', '144h', '192h', '240h']
markerBack, markerBody = 70, 150
# import image sequence with immediate grayscale conversion
# η αρχική ανάλυση της εικόνας είναι (240, 320)
rawImages, readable_EXIF = load_images(name='BAT')
sensorData = load_csv(sampleHours, name='BAT')

# Display purposes: clear the FLIR logo and the pseudo-color scale
# με το κεντράρισμα του ποντικιού ρίχνουμε το μέγεθος σε (240, 144)
cutImages = [mouseImage[:, 100:260] for mouseImage in rawImages]

gif_maker(rawImages, cutImages)

for cutImage, rawImage in zip(cutImages, rawImages):
    # -------------- Figure: 2-figure about the FLIR logo removal --------
    fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    fig.suptitle('Border Removal', fontsize='xx-large')
    grid = fig.add_gridspec(nrows=2, ncols=2, wspace=0.2, hspace=0.2)
    
    ax = fig.add_subplot(grid[0, 0])
    ax.imshow(X=rawImage, cmap=plt.cm.nipy_spectral)
    ax.axvline(x=100, c='red')
    ax.axvline(x=260, c='red')
    ax.set_title(label='Image')
    ax.set_ylabel('Raw Image')
    fig.add_subplot(ax)
    
    ax = fig.add_subplot(grid[0, 1])
    histRaw, histRaw_centers = histogram(img_as_ubyte(rawImage))
    ax.plot(histRaw_centers, histRaw, lw=1)
    ax.set_title(label='Histogram')
    fig.add_subplot(ax)
    
    ax = fig.add_subplot(grid[1, 0])
    ax.imshow(X=cutImage, cmap=plt.cm.nipy_spectral)
    ax.set_ylabel('Cut Image')
    fig.add_subplot(ax)

    ax = fig.add_subplot(grid[1, 1])
    histCut, histCut_centers = histogram(img_as_ubyte(cutImage))
    ax.plot(histCut_centers, histCut, lw=1)
    ax.axvline(x=markerBody, color='red', linestyle='--')
    ax.axvline(x=markerBack, color='blue', linestyle='--')
    ax.axvspan(xmin=markerBody, xmax=255, color='red', alpha=0.15)
    ax.axvspan(xmin=0, xmax=markerBack, color='blue', alpha=0.15)
    fig.add_subplot(ax)

# Preprocessing -- στατιστικά εικόνας, πριν κάνουμε αλλαγές
sigmaEstimatesBefore = [estimate_sigma(mouseImage) for mouseImage in cutImages]
meanBefore = [np.mean(mouseImage) for mouseImage in cutImages]
SNRBefore = list(map(lambda x, y: x / y, meanBefore, sigmaEstimatesBefore))

# downscale + unsharp mask when using a graph-based method due to memory complexity
# εδώ προφανώς θα πέσουμε στα (120, 77)
# preprocessing // αλλαγές: αποκλιμάκωση εικόνας και αφαίρεση θορύβου
mouseImages = [downscale_local_mean(mouseImage, (2, 2)) for mouseImage in cutImages]
# or denoise_wavelet
mouseImages = [unsharp_mask(mouseImage) for mouseImage in mouseImages]

# Preprocessing -- στατιστικά εικόνας, αφού κάνουμε αλλαγές
sigmaEstimatesAfter = [estimate_sigma(mouseImage) for mouseImage in mouseImages]
meanAfter = [np.mean(mouseImage) for mouseImage in mouseImages]
SNRAfter = list(map(lambda x, y: x / y, meanAfter, sigmaEstimatesAfter))
#-------------- Figure: 1-figure with estimated SNR before and after preprocessing --------
fig = plt.figure(figsize=(8, 8), constrained_layout=False)
fig.suptitle('Estimated SNR', fontsize='xx-large')
grid = fig.add_gridspec(nrows=1, ncols=1, wspace=0.1, hspace=0.1)

ax = fig.add_subplot(grid[0, 0])
ax.grid(True)
ax.set_xticks(ticks=np.arange(0, 9, 1))
ax.set_xticklabels(labels=sampleHours)
ax.set_xlabel(xlabel='Sample Hours')

ax.plot(np.arange(0, 9, 1), SNRBefore, 'k--', 
        label='Cut Images')
ax.scatter(np.arange(0, 9, 1), SNRBefore, c='black', s=10)
ax.legend(loc='best', shadow=True, fontsize='x-large')

ax.plot(np.arange(0, 9, 1), SNRAfter, 'k', 
        label='Downscale \n + Denoise')
ax.scatter(np.arange(0, 9, 1), SNRAfter, c='black', s=10)
ax.legend(loc='best', shadow=True, fontsize='x-large')
fig.add_subplot(ax)


minMouseImages, mouseMasks = 9*[], 9*[]
for index, (cutImage, sampleHour) in enumerate(zip(mouseImages, sampleHours)):
    print(f'=============== sample of {sampleHour} ==================')
    # ===================== 1. Region-based background segmentation ============================
    # this mask is going to be topologically processed for the tissue segmentation
    # either the BAT which is close to the back neck, or WAT which is close to the belly
    # Κάνουμε μια region-based μέθοδο χρησιμοποιώντας την κατάτμηση watershed για μια binary μάσκα.

    # We create markers indicating the segmentation through histogram values
    markerImage = np.zeros_like(cutImage)

    # We find markers of the background and the mouse body based on the extreme
    # parts of the histogram of gray values.  μαρκάρω == marker, πινακιδιάζω == label
    
    markerImage[img_as_ubyte(cutImage) < markerBack] = 1
    markerImage[img_as_ubyte(cutImage) > markerBody] = 2
    # We use the watershed transform to fill regions of the elevation
    # map starting from the markers determined above
    # find an elevation map using the image Sobel gradient.
    elevationMap = sobel(cutImage)
    initialMaskTemp = watershed(elevationMap, markerImage)

    # This method segments and labels the mouse individually
    initialMask = ndi.binary_fill_holes(initialMaskTemp - 1)

    # binary labeling, object and background 
    labeledMouse, _ = ndi.label(initialMask)
    # βρήκαμε ένα αντικείμενο -ωραία
    # επιστρέφει έναν τύπο δεδομένων, που λέγεται slice, ένα τετράγωνο μέσα στην αρχική εικόνα
    # είναι σαν generator range object, με διάφορα attributes / methods
    mouseLocation = ndi.find_objects(labeledMouse)[0]

    fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    fig.suptitle('Background Segmentation / Binary Mask', fontsize='xx-large')
    grid = fig.add_gridspec(nrows=2, ncols=2, wspace=0.2, hspace=0.25)
    
    ax = fig.add_subplot(grid[0, 0])
    ax.imshow(X=markerImage, cmap=plt.cm.nipy_spectral)
    ax.set_title(label='1. Hist. Marking')
    fig.add_subplot(ax)
    
    ax = fig.add_subplot(grid[0, 1])
    ax.imshow(X=elevationMap)
    ax.set_title(label='2. Elevation Map')
    fig.add_subplot(ax)
    
    ax = fig.add_subplot(grid[1, 0])
    ax.imshow(X=initialMaskTemp, cmap=plt.cm.nipy_spectral)
    ax.set_title(label='3. Watershed Segmentation')
    fig.add_subplot(ax)

    ax = fig.add_subplot(grid[1, 1])
    ro, co = rectangle_perimeter(start=(mouseLocation[0].start, mouseLocation[1].start),
                                 end=(mouseLocation[0].stop, mouseLocation[1].stop),
                                 shape=cutImage.shape)
    initialMask[ro, co] = True
    ax.imshow(X=initialMask)
    ax.set_title(label='4. Binary Fill \n + BBox')
    fig.add_subplot(ax)

    # Μειώνουμε και άλλο την εικονα στο ακριβες κουτι του ποντικιου
    mouseImage = cutImage[mouseLocation]
    mouseMask = initialMask[mouseLocation]
    minMouseImages.append(mouseImage)
    mouseMasks.append(mouseMask)


n_clusters, n_features = 6, 2
# Fixing random state for reproducibility
np.random.seed(0)
# για το αρχικό clustering.Kmeans() iteration, στη συνέχεια αλλάζει τύπο και γίνεται τα κεντροειδή
CENTROIDS = 'k-means++'
# για την παράμετρο της μεθόδου της υφής
METHOD = ('uniform', 'default', 'ror', 'var')
clusteringScores, n_samplesList = [], []
for index, (mouseMask, mouseImage) in enumerate(zip(mouseMasks, minMouseImages)):
    
    # μάσκα ποντικιού και ανάλυση σε διανύσματα συντεταγμένων
    maskOrdinateX, maskOrdinateY = img_to_vectors(mouseMask)
    n_samples = maskOrdinateX.size # == maskOrdinateY.size => mouse area 
    n_samplesList.append(n_samples)
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

    # ανίχνευση με κατασκευή παράθυρου, όπου θα φτιάξουμε το εμβαδόν του
    # inter-scapular = δια-ωμοπλατιαίος
    # πού είν' τ'αυτιά; -εκεί είναι τα όρια της ωμοπλάτης, κάτω από τη μέση
    # σε ένα σημείο το οριζόντιο μήκος πέφτει, άρα υπολογίζουμε τα οριζόντια μήκη για αρχή από τη μάσκα

    # print(sum(mouseMask, axis=0))

    #-------------- Figure: 5-figure 1. elevation map 2. markers 3. mask 4. skeleton 5. thin --------
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # fig.suptitle(sampleHour + 'samples/mouseArea')
    # grid = fig.add_gridspec(nrows=2, ncols=3, wspace=0.15, hspace=0.2)
    # ro, co = rectangle_perimeter(start=(mouseLocation[0].start, mouseLocation[1].start),
    #                         end=(mouseLocation[0].stop, mouseLocation[1].stop),
    #                         shape=cutImage.shape)
    
    # ax = fig.add_subplot(grid[0, 0])
    # elevationMap[ro, co] = 1.0
    # ax.imshow(X=elevationMap, cmap=plt.cm.gray)
    # ax.set_title(label='Elevation Map')
    # fig.add_subplot(ax)
    
    # ax = fig.add_subplot(grid[0, -1])
    # ax.imshow(X=markerImage, cmap=plt.cm.gray)
    # ax.set_title(label='Hist. Markers')
    # fig.add_subplot(ax)
    
    # ax = fig.add_subplot(grid[1, 0])
    # ax.imshow(X=mouseMask, cmap=plt.cm.gray)
    # ax.scatter(x=maskInfo[0].centroid[1], y=maskInfo[0].centroid[0], c='red', s=3)
    # ax.set_title(label='Mask Image')
    # fig.add_subplot(ax)
    
    # ax = fig.add_subplot(grid[1, 1])
    # ax.imshow(X=skeletonImage, cmap=plt.cm.gray)
    # ax.contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # # ax.xticks([])
    # ax.set_title(label='Skeleton over Mask')
    # fig.add_subplot(ax)
    
    # ax = fig.add_subplot(grid[1, 2])
    # ax.imshow(X=thinImage, cmap=plt.cm.gray)
    # ax.contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # # ax.xticks([])
    # ax.set_title(label='Thin over Mask')
    # fig.add_subplot(ax)

    # #-------------- Figure: 3-figure considered with the background/object segmentation --------
    
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # fig.suptitle('Histogram and Entropy')
    # grid = fig.add_gridspec(nrows=2, ncols=2, wspace=0.25, hspace=0.25)
    
    # ax = fig.add_subplot(grid[0, 0])
    # img1 = ax.imshow(X=img_as_ubyte(mouseImage), cmap=plt.cm.nipy_spectral)
    # ax.contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # ax.set_title(label='Bounded Image')
    # fig.colorbar(img1, ax=ax)
    # fig.add_subplot(ax)
    
    # ax = fig.add_subplot(grid[0, 1])
    # img1 = ax.imshow(X=entropy(image=img_as_ubyte(mouseImage), selem=disk(5), mask=mouseMask),
    #                  cmap=plt.cm.nipy_spectral_r)
    # ax.contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    # ax.set_title(label='Entropy')
    # fig.colorbar(img1, ax=ax)
    # fig.add_subplot(ax)
    
    # hist, hist_centers = histogram(img_as_ubyte(mouseImage) * mouseMask)
    # ax = fig.add_subplot(grid[1, :])
    # ax.plot(hist_centers[1:], hist[1:], lw=1)
    # ax.set_title(label='Image histogram')
    # ax.set_xticks(ticks=np.arange(0, 255, 20))
    # fig.add_subplot(ax)

    # ===================== 2. Body-Tissue Clustering Stage ========================================
    #-------------- Creating / Selecting clustering Features  ----------------------------
    # todo: find more features to cluster, like the image texture

    # κατασκευή του διανύσματος feature για τον αλγόριθμο συσταδοποίησης
    # mouse intensity made into a vector of length {n_samples}
    intensityFeature = np.zeros(n_samples, dtype='float64') 
    # mouseImage_ubyte = img_as_ubyte(mouseImage)
    # for i in range(n_samples):
    #     intensityFeature[i] = mouseImage[maskOrdinateX[i], maskOrdinateY[i]]
    mouseImage255 = img_as_ubyte(mouseImage)
    intensityFeature = mouseImage255[maskOrdinateX, maskOrdinateY]

    # segmentedImage: εικόνα διάστασης mouseImage με μαύρο background
    segmentedImage = np.zeros_like(mouseImage)
    for i in range(n_samples):
        segmentedImage[maskOrdinateX[i]][maskOrdinateY[i]] = intensityFeature[i]

    # βγάζω την εικόνα texture για να την περάσω ως feature προς τη μέθοδο συσταδοποίησης
    radius = 10
    n_points = 8 * radius + 4
    textureImage = local_binary_pattern(image=segmentedImage, P=n_points, R=radius, method=METHOD[0])
    # textureImage = textureImage.astype('int')
    # textureImage = img_as_float(textureImage)

    # mouse texture made into a vector of length {n_samples}
    textureFeature = np.zeros(n_samples)
    textureFeature = textureImage[maskOrdinateX, maskOrdinateY]

    # το αντίστροφο να φτιάξουμε μια εικόνα μέσω της μάσκας
    segmentedTexture = np.zeros_like(segmentedImage)
    for i in range(n_samples):
        segmentedTexture[maskOrdinateX[i]][maskOrdinateY[i]] = textureFeature[i]

    #-------------- Figure: 4-figure comparing texture and intensity histogram  --------
    # textureFeature, bins=np.max(textureFeature), range=(0,255)
    
    fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    fig.suptitle('Pre Scaled Features')
    grid = fig.add_gridspec(nrows=2, ncols=2, wspace=0.15, hspace=0.2)
    
    ax = fig.add_subplot(grid[0, 0])
    img1 = ax.imshow(X=segmentedImage, cmap=plt.cm.nipy_spectral)
    ax.contour(mouseMask, [0.5], linewidths=1.2, colors='w')
    fig.colorbar(img1, ax=ax)
    ax.set_title(label='Feature')
    ax.set_ylabel('Intensity')
    
    ax = fig.add_subplot(grid[0, 1])
    histIntensity, hist_centersIntensity = histogram(img_as_ubyte(mouseImage) * mouseMask)
    ax.plot(hist_centersIntensity[1:], histIntensity[1:], lw=1)
    ax.set_title(label='Histogram')
    
    ax = fig.add_subplot(grid[1, 0])
    img1 = ax.imshow(X=segmentedTexture, cmap=plt.cm.nipy_spectral)
    fig.colorbar(img1, ax=ax)
    ax.set_ylabel('Texture')
    
    ax = fig.add_subplot(grid[1, 1])
    histTexture, hist_centersTexture = histogram(textureImage * mouseMask)
    ax.plot(hist_centersTexture[1:-1], histTexture[1:-1], lw=1)
    
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
    #--------------- 2a Feature Scaling Methods ---------------------------------
    
    scaler = preprocessing.RobustScaler()
    # scaler = preprocessing.MaxAbsScaler()
    # scaler = preprocessing.Normalizer()
    # scaler = preprocessing.StandardScaler()
    # scaler = preprocessing.MinMaxScaler()
    X = scaler.fit_transform(X)
    # tweaking the hyperparameter
    lamdaHyperparameter = 10.0
    X[:, 1] = np.sqrt(lamdaHyperparameter) * X[:, 1]

    # ------------------- 2. Clustering Methods ----------------------------------
    # ------------------- Distanced based: Kmeans --------------------------------
    kMeans = cluster.KMeans(n_clusters=n_clusters)
    kMeans.fit(X)
    CENTROIDS = kMeans.cluster_centers_.squeeze() # no random init at next iteration
    # print('Distance-based mouse centroids are ', CENTROIDS)
    labels = kMeans.labels_

    # ------------------- Density based: Mean Shift ----------------------
    # meanShift = cluster.MeanShift()
    # meanShift.fit(X)
    # CENTROIDS = meanShift.cluster_centers_.squeeze()
    # print('Density-based mouse centroids are ', CENTROIDS)
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
    # ομοιότητα : affinity  είναι ένας similarity πίνακας, με όλους τους συνδυασμούς των δειγμάτων
    # affinity = spectral.affinity_matrix_.toarray()
    # labels = spectral.labels_

    #------------------- 2b Metrics: Internal cluster evaluation  -----------
    score = (silhouette_score(X, labels),
             calinski_harabasz_score(X, labels),
             davies_bouldin_score(X, labels))
    clusteringScores.append(score)

    # # original-sized image, with the labels + 1 given by the clustering algorithms
    # labeledImage = np.zeros_like(mouseImage, dtype='int')
    # for i in range(n_samples):
    #     labeledImage[maskOrdinateX[i]][maskOrdinateY[i]] = labels[i] + 1

    # # η παρακάτω λίστα είναι σε μήκος όση και τα n_cluster (== label number),
    # # δίνει πληροφορίες για κάθε περιοχή όσον αφορά σε σχήματα από κουτιά,
    # # ειδικά για τις συντεταγμένες τους, τα εμβαδά τους και τα μήκη των καμπυλών
    # clustersInfo = regionprops(label_image=labeledImage, intensity_image=segmentedImage)
    
    # clustersTable = regionprops_table(label_image=labeledImage, intensity_image=segmentedImage)
    # dataframe = pd.DataFrame(clustersTable)
    # # λίστα από δι-tuples με μήκος n_clusters πχ [(80, 12), (40, 13)]
    # # γενικά: info_list = [info.attribute for info in clustersInfo]
    # clusterCentroids = [clusterElement.centroid for clusterElement in clustersInfo]
    # # θα τα κανω scatter plot οπότε σημαίνει δύο λίστες x = [80, 40] y = [12, 13]
    # # άρα τα κάνω unpack με το
    # centroidRow, centroidColumn = map(list, zip(*clusterCentroids))

    # #-------------- Figure: 2-figure of the segmented object values ----------------------------
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # grid = fig.add_gridspec(nrows=1, ncols=3, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(X=segmentedImage, cmap=plt.cm.nipy_spectral)
    # ax.set_title(label='Segmented Image')
    # ax.scatter(x=centroidColumn, y=centroidRow, c='white', s=6)
    
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(X=labeledImage, cmap=plt.cm.nipy_spectral)
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    # ax.set_title(label='Clustered Skeleton')
    
    # ax = fig.add_subplot(grid[0, 2])
    # ax.imshow(X=labeledImage, cmap=plt.cm.nipy_spectral)
    # ax.scatter(x=thinOrdinateY, y=thinOrdinateX, c='white', s=1)
    # ax.set_title(label='Clustered Thin')

    # #================= 3 BAT extraction from the ROI ===============================

    # # ROI contains multiple labels, how do we deal with the exact roi location?
    # # θα κανουμε μια προσεγγιση με το σκελετο ως ραγα για τις περιοχές όπου θα
    # # περάσει το παραθυρο αναζητησης
    # # το παραθυρο αναζητησης εχει ενα σχημα και συγκεντρωνει τα labels φτιαχνοντας ενα ιστογραμμα
    # # σειριακα συγκρινουμε τα ιστογραμματα ως πυκνοτητα πιθανοτητας και βρισκουμε την εντροπια
    # # ή την κοινη πληροφορια τους ως μέτρο σφαλματος
    # # μεχρι να μην ξεπερασουμε τα γεωμετρικά όρια του αυχένα / ωμοπλάτης
    # sample = 70
    # r, c = skeletonOrdinateX[sample], skeletonOrdinateY[sample]
    # rr, cc = rectangle(start=(r, c), extent=(-10, 10), shape=mouseImage.shape)

    # maskBAT = np.zeros_like(segmentedImage)
    # maskBAT[rr, cc] = 1
    # tissueBAT = segmentedImage * maskBAT

    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # fig.suptitle(sampleHour)
    # grid = fig.add_gridspec(nrows=1, ncols=2, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    # ax.contour(maskBAT)
    # ax.set_title('Seed points')
    # ax.scatter(x=centroidColumn, y=centroidRow, c='white', s=6)
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(tissueBAT, cmap=plt.cm.gray)
    # ax.set_title('Seed image')

    # centroidColumn, centroidRow = list(map(int, centroidColumn)), list(map(int, centroidRow))
    # # filter()
    # seedImage = np.zeros_like(segmentedImage)

    # seedImage[centroidRow[1]:centroidRow[1] + 6, centroidColumn[1]:centroidColumn[1] + 6] = 2
    # seedImage[centroidRow[2]:centroidRow[2] + 6, centroidColumn[2]:centroidColumn[2] + 6] = 1

    # seedImage[skeletonOrdinateX[slice(None, skeletonOrdinateX.size // 4)], skeletonOrdinateY[slice(None, skeletonOrdinateY.size // 4)]] = 2
    # seedImage[thinImage] = 1
    # # άμα έχει μέχρι δύο label τότε επιστρέφει για κάθε ένα ξεχωριστό πίνακα με το return_full_prob=True

    # rrr1, ccc1 = rectangle_perimeter(start=(r, c), extent=(-10, -10), shape=seedImage.shape)
    # rrr1, ccc1 = circle_perimeter(r, c, radius=9, shape=seedImage.shape)
    # seedImage[rrr1, ccc1] = 1
    # rrr2, ccc2 = rectangle_perimeter(start=(r, c), extent=(-15, -15), shape=seedImage.shape)
    # rrr2, ccc2 = circle_perimeter(r, c, radius=5, shape=seedImage.shape)
    # seedImage[rrr2, ccc2] = 2

    # # Δοκιμές με τι δεδομένα να κάνουμε την αποκοπή
    # outputIntensity = random_walker(data=segmentedImage, labels=seedImage, beta=80, return_full_prob=False)
    # outputTexture = random_walker(data=textureImage, labels=seedImage, beta=80, return_full_prob=False)
    # outputLabeled = random_walker(data=segmentedImage, labels=labeledImage, beta=80, return_full_prob=False)
    
    # #-------------- Figure: 3-figure of seed points, seed image and result ----------------------------
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # fig.suptitle(sampleHour)
    # grid = fig.add_gridspec(nrows=1, ncols=4, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(labeledImage, cmap=plt.cm.nipy_spectral)
    # ax.set_title('MouseImage')
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(outputLabeled, cmap=plt.cm.nipy_spectral)
    # # ax.contour(outputImage)
    # ax.scatter(x=c, y=r, c='white', s=16)
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    # ax.set_title('BAT labeled')
    
    # ax = fig.add_subplot(grid[0, 2])
    # ax.imshow(segmentedImage, cmap=plt.cm.nipy_spectral)
    # ax.contour(outputIntensity, [0.5], linewidths=1.2, colors='w')
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='white', s=1)
    # ax.set_title('BAT intensity')
    
    # ax = fig.add_subplot(grid[0, 3])
    # ax.imshow(textureImage, cmap=plt.cm.gray)
    # ax.contour(outputTexture, [0.5], linewidths=1.2, colors='w')
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    # ax.set_title('BAT texture')
    
    # # παμε να δοκιμασουμε τελείως morphological επεξεργασία και 
    # oneLabeledImage = np.where(labeledImage == (n_clusters - 1), 0, 1)
    # contours = find_contours(oneLabeledImage, level=0)
    # megalo = contours[0].astype(int)
    
    # eikonamegalo = np.zeros(shape=oneLabeledImage.shape, dtype=bool)
    # eikonamegalo[megalo[:, 0]][megalo[:, 1]] = True
    
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # grid = fig.add_gridspec(nrows=1, ncols=2, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(eikonamegalo, cmap=plt.cm.gray)
    # ax.set_title('one label')
    # ax.scatter(x=megalo[:, 1], y=megalo[:, 0], c='red', s=1)
    
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(oneLabeledImage, cmap=plt.cm.gray)
    # # ax.contour(outputImage)
    # ax.scatter(x=c, y=r, c='white', s=16)
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    # ax.set_title('eliminate boundaries')
    
    # teliko = regionprops(label_image=oneLabeledImage)
    
    # boundaryImage = np.logical_xor(oneLabeledImage, dilation(oneLabeledImage, square(9)))
    
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # grid = fig.add_gridspec(nrows=1, ncols=2, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(X=oneLabeledImage, cmap=plt.cm.gray)
    # ax.set_title(label='one label')
    # ax.scatter(x=megalo[:, 1], y=megalo[:, 0], c='red', s=1)
    
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(X=boundaryImage, cmap=plt.cm.gray)
    # # ax.contour(outputImage)
    # # ax.scatter(x=c, y=r, c='white', s=16)
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    # ax.set_title(label='Eliminate Boundaries')
    
    # fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    # fig.suptitle(sampleHour)
    # grid = fig.add_gridspec(nrows=1, ncols=2, wspace=0.15, hspace=0.2)
    
    # ax = fig.add_subplot(grid[0, 0])
    # ax.imshow(X=oneLabeledImage, cmap=plt.cm.gray)
    # ax.set_title(label='one label')
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    
    # ax = fig.add_subplot(grid[0, 1])
    # ax.imshow(X=boundaryImage, cmap=plt.cm.gray)
    # # ax.contour(outputImage)
    # # ax.scatter(x=c, y=r, c='white', s=16)
    # ax.scatter(x=skeletonOrdinateY, y=skeletonOrdinateX, c='red', s=1)
    # ax.set_title(label='Eliminate Boundaries')
    
    

# clusteringScores λίστα από 3-tuples με μήκος n_clusters 
# πχ [(80, 12, 16), (40, 13, 17)]
# allScores = [score for score in clusteringScores]
# θα τα κανω scatter plot οπότε σημαίνει 3 λίστες
# x = [80, 40] y = [12, 13] z = [16, 17] άρα τα κάνω unpack με το
silhouette, calinski, davies = map(list, zip(*clusteringScores))

meanScores = list(map(np.mean, (silhouette, calinski, davies, n_samplesList)))
#-------------- Figure: 1-figure comparing the clustering scores with their mean values  --------
fig = plt.figure(figsize=(8, 8), constrained_layout=False)

fig.suptitle(f'Utilized {n_features} features \n and {n_clusters} clusters')
grid = fig.add_gridspec(nrows=4, ncols=1, wspace=0.25, hspace=0.1)

ax = fig.add_subplot(grid[0])
ax.grid(True)
ax.plot(np.arange(0, 9, 1), silhouette, 'k', label='Silh. Score')
ax.scatter(np.arange(0, 9, 1), silhouette, c='black', s=10)
ax.set_xticks(ticks=np.arange(0, 9, 1))
ax.set_xticklabels(labels=[])
ax.axhline(y=meanScores[0], color='r', linestyle='--', 
           label='Mean '+"{:.2f}".format(meanScores[0]))
ax.legend(loc='best', shadow=True, fontsize='large')
fig.add_subplot(ax)

ax = fig.add_subplot(grid[1])
ax.grid(True)
ax.plot(np.arange(0, 9, 1), davies, 'k', label='D-B Index')
ax.scatter(np.arange(0, 9, 1), davies, c='black', s=10)
ax.set_xticks(ticks=np.arange(0, 9, 1))
ax.set_xticklabels(labels=[])
ax.axhline(y=meanScores[2], color='r', linestyle='--', 
           label='Mean '+"{:.2f}".format(meanScores[2]))
ax.legend(loc='best', shadow=True, fontsize='large')

fig.add_subplot(ax)

ax = fig.add_subplot(grid[2])
ax.grid(True)
ax.plot(np.arange(0, 9, 1), calinski, 'k', label='C-H Index')
ax.scatter(np.arange(0, 9, 1), calinski, c='black', s=10)
ax.set_xticks(ticks=np.arange(0, 9, 1))
ax.set_xticklabels(labels=[])
ax.axhline(y=meanScores[1], color='r', linestyle='--', 
           label='Mean '+"{:.2f}".format(meanScores[1]))
ax.legend(loc='best', shadow=True, fontsize='large')
fig.add_subplot(ax)

ax = fig.add_subplot(grid[3])
ax.grid(True)
ax.plot(np.arange(0, 9, 1), n_samplesList, 'k', label='Mouse Area')
ax.scatter(np.arange(0, 9, 1), n_samplesList, c='black', s=10)
ax.set_xticks(ticks=np.arange(0, 9, 1))
ax.set_xticklabels(labels=sampleHours)
ax.axhline(y=meanScores[3], color='r', linestyle='--', 
            label='Mean '+"{:.2f}".format(meanScores[3]))
ax.legend(loc='best', shadow=True, fontsize='large')
ax.set_xlabel(xlabel='Sample Hours')
fig.add_subplot(ax)