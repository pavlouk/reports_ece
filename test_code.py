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
import numpy as np
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



def overplot(func):
    def testplot_wrapper():
        x, y = np.linspace(0,5), np.linspace(0,10)
        plt.plot(x,y)
        print('asterakia mou')
        func()
    return(testplot_wrapper)

@overplot
def testplot():
    x, y = np.linspace(0,5), np.linspace(0,5)
    print('ajjjjjjjjjj')
    plt.plot(x,y) 

testplot()
plt.show()




fig3 = plt.figure(constrained_layout=True)
gs = fig3.add_gridspec(3, 3)
f3_ax1 = fig3.add_subplot(np.arange(0, 9, 1), silhouette, 'k--', label='silhouette')
f3_ax1.set_title('gs[0, :]')
f3_ax2 = fig3.add_subplot(gs[1, :-1])
f3_ax2.set_title('gs[1, :-1]')
f3_ax3 = fig3.add_subplot(gs[1:, -1])
f3_ax3.set_title('gs[1:, -1]')
f3_ax4 = fig3.add_subplot(gs[-1, 0])
f3_ax4.set_title('gs[-1, 0]')
f3_ax5 = fig3.add_subplot(gs[-1, -2])
f3_ax5.set_title('gs[-1, -2]')




import numpy as np
from itertools import product


def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.05)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)


fig11 = plt.figure(figsize=(8, 8), constrained_layout=False)

# gridspec inside gridspec
outer_grid = fig11.add_gridspec(nrows=4, ncols=4, wspace=0.2, hspace=0.3)

for i in range(16):
    inner_grid = outer_grid[i].subgridspec(nrows=3, ncols=3, wspace=0.1, hspace=0.2)
    a, b = int(i/4)+1, i % 4+1
    for j, (c, d) in enumerate(product(range(1, 4), repeat=2)):
        ax = fig11.add_subplot(inner_grid[j])
        ax.plot(*squiggle_xy(a, b, c, d))
        ax.set_xticks([])
        ax.set_yticks([])
        fig11.add_subplot(ax)

all_axes = fig11.get_axes()

# show only the outside spines
for ax in all_axes:
    for sp in ax.spines.values():
        sp.set_visible(False)
    if ax.is_first_row():
        ax.spines['top'].set_visible(True)
    if ax.is_last_row():
        ax.spines['bottom'].set_visible(True)
    if ax.is_first_col():
        ax.spines['left'].set_visible(True)
    if ax.is_last_col():
        ax.spines['right'].set_visible(True)

plt.show()

