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



from PIL import Image, ImageDraw

images = []

width = 200
center = width // 2
color_1 = (0, 0, 0)
color_2 = (255, 255, 255)
max_radius = int(center * 1.5)
step = 8

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_1)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_2)
    images.append(im)

for i in range(0, max_radius, step):
    im = Image.new('RGB', (width, width), color_2)
    draw = ImageDraw.Draw(im)
    draw.ellipse((center - i, center - i, center + i, center + i), fill=color_1)
    images.append(im)

images[0].save('llow_imagedraw.gif', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)



################################################################
import matplotlib
matplotlib.use('Qt5Agg') #use Qt5 as backend, comment this line for default backend

from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()

ax = plt.axes(xlim=(0, 2), ylim=(0, 100))

N = 4
lines = [plt.plot([], [])[0] for _ in range(N)] #lines to animate

rectangles = plt.bar(x=[0.5,1,1.5], height=[50,40,90], width=0.1) #rectangles to animate

patches = lines + list(rectangles) #things to animate

def init():
    #init lines
    for line in lines:
        line.set_data([], [])

    #init rectangles
    for rectangle in rectangles:
        rectangle.set_height(0)

    return patches #return everything that must be updated

def animate(i):
    #animate lines
    for j,line in enumerate(lines):
        line.set_data([0, 2], [10 * j,i])

    #animate rectangles
    for j,rectangle in enumerate(rectangles):
        rectangle.set_height(i/(j+1))

    return patches #return everything that must be updated

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

plt.show()



