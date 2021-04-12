import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from skimage.exposure import histogram
from skimage.util import img_as_ubyte

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

def cut_uncut_compare(rawImages, cutImages, markerBack=70, markerBody=150):
    print(f'{rawImages[0].shape}')
    for rawImage, cutImage in zip(rawImages, cutImages):
        # -------------- Figure: 2-figure about the FLIR logo removal --------
        fig = plt.figure(figsize=(8, 8), constrained_layout=False)
        fig.suptitle(t='Border Removal', fontsize='xx-large')
        grid = fig.add_gridspec(nrows=2, ncols=2, wspace=0.2, hspace=0.2)
        
        ax = fig.add_subplot(grid[0, 0])
        ax.imshow(X=rawImage, cmap=plt.cm.nipy_spectral)
        ax.axvline(x=100, c='red')
        ax.axvline(x=260, c='red')
        ax.set_title(label='Image')
        ax.set_ylabel(ylabel='Raw Image')
        fig.add_subplot(ax)
        
        ax = fig.add_subplot(grid[0, 1])
        histRaw, histRaw_centers = histogram(img_as_ubyte(rawImage))
        ax.plot(histRaw_centers, histRaw, lw=1)
        ax.set_title(label='Histogram')
        fig.add_subplot(ax)
        
        ax = fig.add_subplot(grid[1, 0])
        ax.imshow(X=cutImage, cmap=plt.cm.nipy_spectral)
        ax.set_ylabel(ylabel='Cut Image')
        fig.add_subplot(ax)
    
        ax = fig.add_subplot(grid[1, 1])
        histCut, histCut_centers = histogram(img_as_ubyte(cutImage))
        ax.plot(histCut_centers, histCut, lw=1)
        ax.axvline(x=markerBody, color='red', linestyle='--')
        ax.axvline(x=markerBack, color='blue', linestyle='--')
        ax.axvspan(xmin=markerBody, xmax=255, color='red', alpha=0.15)
        ax.axvspan(xmin=0, xmax=markerBack, color='blue', alpha=0.15)
        fig.add_subplot(ax)
    return fig
        
def snr_print(sampleHours, mouseImages, cutImages):
    # Preprocessing -- στατιστικά εικόνας, πριν κάνουμε αλλαγές
    sigmaEstimatesBefore = [estimate_sigma(mouseImage) for mouseImage in cutImages]
    meanBefore = [np.mean(mouseImage) for mouseImage in cutImages]
    SNRBefore = list(map(lambda x, y: x / y, meanBefore, sigmaEstimatesBefore))
    # Preprocessing -- στατιστικά εικόνας, αφού κάνουμε αλλαγές
    sigmaEstimatesAfter = [estimate_sigma(mouseImage) for mouseImage in mouseImages]
    meanAfter = [np.mean(mouseImage) for mouseImage in mouseImages]
    SNRAfter = list(map(lambda x, y: x / y, meanAfter, sigmaEstimatesAfter))
    #-------------- Figure: 1-figure with estimated SNR before and after preprocessing --------
    fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    fig.suptitle(t='Estimated SNR', fontsize='xx-large')
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
    
def clustering_scores(clusteringScores, n_samplesList, sampleHours, n_features, n_clusters):
    # clusteringScores λίστα από 3-tuples με μήκος n_clusters 
    # πχ [(80, 12, 16), (40, 13, 17)]
    # allScores = [score for score in clusteringScores]
    # θα τα κανω scatter plot οπότε σημαίνει 3 λίστες
    # x = [80, 40] y = [12, 13] z = [16, 17] άρα τα κάνω unpack με το
    silhouette, calinski, davies = map(list, zip(*clusteringScores))
    
    meanScores = list(map(np.mean, (silhouette, calinski, davies, n_samplesList)))
    #-------------- Figure: 1-figure comparing the clustering scores with their mean values  --------
    fig = plt.figure(figsize=(8, 8), constrained_layout=False)
    
    fig.suptitle(t=f'Utilized {n_features} features \n and {n_clusters} clusters')
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