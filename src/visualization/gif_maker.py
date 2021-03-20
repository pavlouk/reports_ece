import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class UpdateDist:
    def __init__(self, ax, list1):
        self.line, = ax.plot([], [], 'k-')
        self.ax = ax
        self.list1 = list1
        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
    def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        # if i == 0:
        #     self.line.set_data([], [])
        #     return self.line,       
        self.ax.axvline(x=100, linestyle='--', color='red')
        self.ax.axvline(x=260, linestyle='--', color='red')
        return self.ax.imshow(self.list1[i], cmap=plt.cm.nipy_spectral),
        #return self.line,
        # επιστρέφει με κομμα γιατί να είναι generator
def gif_maker(image_list1, image_list2):
    
    fig = plt.figure(figsize=(8, 8), constrained_layout=True)
    fig.suptitle('Border Removal', fontsize='xx-large')
    grid = fig.add_gridspec(nrows=1, ncols=2, wspace=0.1, hspace=0.1)
    # 1. πώς λειτουργεί τo FuncAnimation
    #  fig το figure object 
    #  ud: callable object μέσω  __call__
    #  frames: int για το __call__
    #  interval: Delay between frames in milliseconds
    #  blit: optimizing drawing
    
    ax1 = fig.add_subplot(grid[0, 0])
    ud1 = UpdateDist(ax1, image_list1)
    ax2 = fig.add_subplot(grid[0, 1])
    ud2 = UpdateDist(ax2, image_list2) # object με call μέθοδο και καστομ constructor
    anim = FuncAnimation(fig, ud1, frames=9, interval=700, blit=True)
    anim = FuncAnimation(fig, ud2, frames=9, interval=700, blit=True)
    
    plt.show()
    
    return None 