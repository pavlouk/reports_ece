# # #!/usr/bin/python
# # # -*- coding: utf-8 -*-

# from sklearn.datasets import make_circles
# from sklearn.neighbors import kneighbors_graph
# import numpy as np

# # create the data
# X, labels = make_circles(n_samples=500, noise=0.1, factor=.2)

# # use the nearest neighbor graph as our adjacency matrix
# A = kneighbors_graph(X, n_neighbors=5).toarray()
# print(A)

# # [[0. 0. 0. ... 0. 0. 0.]
# #  [0. 0. 0. ... 0. 0. 0.]
# #  [0. 0. 0. ... 0. 0. 0.]
# #  ...
# #  [0. 0. 0. ... 0. 1. 0.]
# #  [0. 0. 0. ... 0. 0. 0.]
# #  [0. 0. 0. ... 0. 0. 0.]]
 
# # create the graph laplacian
# D = np.diag(A.sum(axis=1))
# L = D-A

# # find the eigenvalues and eigenvectors
# vals, vecs = np.linalg.eig(L)

# # sort
# vecs = vecs[:,np.argsort(vals)]
# vals = vals[np.argsort(vals)]

# # use Fiedler value to find best cut to separate data
# clusters = vecs[:,1] > 0

# import matplotlib.pyplot as plt

# from skimage import data, color
# from skimage.transform import rescale, resize, downscale_local_mean

# image = color.rgb2gray(data.astronaut())

# image_rescaled = rescale(image, 0.25, anti_aliasing=False)
# image_resized = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
#                        anti_aliasing=True)
# image_downscaled = downscale_local_mean(image, (4, 4))

# fig, axes = plt.subplots(nrows=2, ncols=2)

# ax = axes.ravel()

# ax[0].imshow(image, cmap='gray')
# ax[0].set_title("Original image")

# ax[1].imshow(image_rescaled, cmap='gray')
# ax[1].set_title("Rescaled image (aliasing)")

# ax[2].imshow(image_resized, cmap='gray')
# ax[2].set_title("Resized image (no aliasing)")

# ax[3].imshow(image_downscaled, cmap='gray')
# ax[3].set_title("Downscaled image (no aliasing)")

# ax[0].set_xlim(0, 512)
# ax[0].set_ylim(512, 0)
# plt.tight_layout()
# plt.show()

# from skimage.segmentation import random_walker
# from skimage.data import binary_blobs
# from skimage.exposure import rescale_intensity
# import skimage

# # Generate noisy synthetic data
# data = skimage.img_as_float(binary_blobs(length=128, seed=1))
# sigma = 0.35
# data += np.random.normal(loc=0, scale=sigma, size=data.shape)
# data = rescale_intensity(data, in_range=(-sigma, 1 + sigma),
#                          out_range=(-1, 1))

# # The range of the binary image spans over (-1, 1).
# # We choose the hottest and the coldest pixels as markers.
# markers = np.zeros(data.shape, dtype=np.uint)
# markers[data < -0.95] = 1
# markers[data > 0.95] = 2

# # Run random walker algorithm
# labels = random_walker(data, markers, beta=10, mode='bf')

# # Plot results
# fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.2),
#                                     sharex=True, sharey=True)
# ax1.imshow(data, cmap='gray')
# ax1.axis('off')
# ax1.set_title('Noisy data')
# ax2.imshow(markers, cmap='magma')
# ax2.axis('off')
# ax2.set_title('Markers')
# ax3.imshow(labels, cmap='gray')
# ax3.axis('off')
# ax3.set_title('Segmentation')

# fig.tight_layout()
# plt.show()

# from __future__ import print_function
# import numpy as np
# import matplotlib.pyplot as plt


# METHOD = 'uniform'
# plt.rcParams['font.size'] = 9


# def plot_circle(ax, center, radius, color):
#     circle = plt.Circle(center, radius, facecolor=color, edgecolor='0.5')
#     ax.add_patch(circle)


# def plot_lbp_model(ax, binary_values):
#     """Draw the schematic for a local binary pattern."""
#     # Geometry spec
#     theta = np.deg2rad(45)
#     R = 1
#     r = 0.15
#     w = 1.5
#     gray = '0.5'

#     # Draw the central pixel.
#     plot_circle(ax, (0, 0), radius=r, color=gray)
#     # Draw the surrounding pixels.
#     for i, facecolor in enumerate(binary_values):
#         x = R * np.cos(i * theta)
#         y = R * np.sin(i * theta)
#         plot_circle(ax, (x, y), radius=r, color=str(facecolor))

#     # Draw the pixel grid.
#     for x in np.linspace(-w, w, 4):
#         ax.axvline(x, color=gray)
#         ax.axhline(x, color=gray)

#     # Tweak the layout.
#     ax.axis('image')
#     ax.axis('off')
#     size = w + 0.2
#     ax.set_xlim(-size, size)
#     ax.set_ylim(-size, size)


# fig, axes = plt.subplots(ncols=5, figsize=(7, 2))

# titles = ['flat', 'flat', 'edge', 'corner', 'non-uniform']

# binary_patterns = [np.zeros(8),
#                     np.ones(8),
#                     np.hstack([np.ones(4), np.zeros(4)]),
#                     np.hstack([np.zeros(3), np.ones(5)]),
#                     [1, 0, 0, 1, 1, 1, 0, 0]]

# for ax, values, name in zip(axes, binary_patterns, titles):
#     plot_lbp_model(ax, values)
#     ax.set_title(name)
    
# # =============================================================================
    
# # =============================================================================
# from skimage.transform import rotate
# from skimage.feature import local_binary_pattern
# from skimage import data
# from skimage.color import label2rgb

# # settings for LBP
# radius = 3
# n_points = 8 * radius


# def overlay_labels(image, lbp, labels):
#     mask = np.logical_or.reduce([lbp == each for each in labels])
#     return label2rgb(mask, image=image, bg_label=0, alpha=0.5)


# def highlight_bars(bars, indexes):
#     for i in indexes:
#         bars[i].set_facecolor('r')


# image = data.load('brick.png')
# lbp = local_binary_pattern(image, n_points, radius, METHOD)


# def hist(ax, lbp):
#     n_bins = int(lbp.max() + 1)
#     return ax.hist(lbp.ravel(), normed=True, bins=n_bins, range=(0, n_bins),
#                    facecolor='0.5')


# # plot histograms of LBP of textures
# fig, (ax_img, ax_hist) = plt.subplots(nrows=2, ncols=3, figsize=(9, 6))
# plt.gray()

# titles = ('edge', 'flat', 'corner')
# w = width = radius - 1
# edge_labels = range(n_points // 2 - w, n_points // 2 + w + 1)
# flat_labels = list(range(0, w + 1)) + list(range(n_points - w, n_points + 2))
# i_14 = n_points // 4            # 1/4th of the histogram
# i_34 = 3 * (n_points // 4)      # 3/4th of the histogram
# corner_labels = (list(range(i_14 - w, i_14 + w + 1)) +
#                  list(range(i_34 - w, i_34 + w + 1)))

# label_sets = (edge_labels, flat_labels, corner_labels)

# for ax, labels in zip(ax_img, label_sets):
#     ax.imshow(overlay_labels(image, lbp, labels))

# for ax, labels, name in zip(ax_hist, label_sets, titles):
#     counts, _, bars = hist(ax, lbp)
#     highlight_bars(bars, labels)
#     ax.set_ylim(ymax=np.max(counts[:-1]))
#     ax.set_xlim(xmax=n_points + 2)
#     ax.set_title(name)

# ax_hist[0].set_ylabel('Percentage')
# for ax in ax_img:
#     ax.axis('off')    

from skimage import data, segmentation
from skimage.future import graph
from matplotlib import pyplot as plt


img = data.coffee()
labels = segmentation.slic(img, compactness=30, n_segments=400)
g = graph.rag_mean_color(img, labels)

fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True, figsize=(6, 8))

ax[0].set_title('RAG drawn with default settings')
lc = graph.show_rag(labels, g, img, ax=ax[0])
# specify the fraction of the plot area that will be used to draw the colorbar
fig.colorbar(lc, fraction=0.03, ax=ax[0])

ax[1].set_title('RAG drawn with grayscale image and viridis colormap')
lc = graph.show_rag(labels, g, img,
                    img_cmap='gray', edge_cmap='viridis', ax=ax[1])
fig.colorbar(lc, fraction=0.03, ax=ax[1])

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()