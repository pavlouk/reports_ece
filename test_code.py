# # -*- coding: utf-8 -*-
# from matplotlib import pyplot as plt, patches
# import os


# def main():
#     for i in range(21):
#         print('Batch {}'.format(i))
#         make_plots('figures')
#     print('Done.')


# def make_plots(path):
#     fig, ax = plt.subplots()
#     for i in range(21):
#         x = range(3 * i)
#         y = [n * n for n in x]
#         ax.add_patch(patches.Rectangle(xy=(i, 1), width=i, height=10))
#         plt.step(x, y, linewidth=2, where='mid')
#         figname = 'fig_{}.png'.format(i)
#         dest = os.path.join(path, figname)
#         plt.savefig(dest)  # write image to file
#         plt.cla()
#     plt.close(fig)


# main()

# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation

# nx = 150
# ny = 50

# fig = plt.figure()
# data = np.zeros((nx, ny))
# im = plt.imshow(data, cmap='gist_gray_r', vmin=0, vmax=1)

# def init():
#     im.set_data(np.zeros((nx, ny)))

# def animate(i):
#     xi = i // ny
#     yi = i % ny
#     data[xi, yi] = 1
#     im.set_data(data)
#     return im

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=nx * ny, interval=50)
# anim.save(filename='afafa.mp4', writer='ffmpeg')

import matplotlib.pyplot as plt

from skimage import data
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage.util import img_as_ubyte


image = img_as_ubyte(data.camera())

fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 4))

img0 = ax0.imshow(image, cmap=plt.cm.gray)
ax0.set_title('Image')
ax0.axis('off')
fig.colorbar(img0, ax=ax0)

img1 = ax1.imshow(entropy(image, disk(5)), cmap=plt.cm.jet)
ax1.set_title('Entropy')
ax1.axis('off')
fig.colorbar(img1, ax=ax1)

plt.show()