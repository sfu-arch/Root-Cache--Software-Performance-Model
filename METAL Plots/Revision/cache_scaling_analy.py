import sys

import math


from matplotlib import pyplot as plt
plt.style.use('ggplot')
import matplotlib as mpl
import matplotlib
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.ticker as ticker
import csv


mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

font = 16

# Fixing random state for reproducibility
# np.random.seed(19680801)

x_pos = [0,1,5,8,9]
cache =['8','16','32','64','128','256']
Speedup_16w =[5.31,9.87,18.13,36.77,39.31,39.81]
Speedup_32w =[10.81,19.78,33.41,65.56,67.71,69.91]
Speedup_64w=[17.17,26.99,45.21,98.17,107.61,108.31]
Speedup_128w=[19.6,34.13,47.17,101.31,109.51,110.71]
fig,ax=plt.subplots(figsize=(8, 5.5))
ax.set_facecolor('w')
ax.set_axisbelow(True)

plt.scatter(cache, Speedup_16w, marker='^',s=80)
plt.scatter(cache, Speedup_32w, marker='o',s=80)
plt.scatter(cache, Speedup_64w, marker='+',s=80)
plt.scatter(cache, Speedup_128w, marker='v',s=80)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')

ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
plt.xlabel('Cache Size (in kB)',size=font, color='k')
plt.ylabel('Norm. Speed Up', size=font, color='k')
plt.legend(["16 Tiles","32 Tiles","64 Tiles","128 Tiles"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=4)
plt.savefig('Plots/pdfs/cache_scaling_analy.pdf')
plt.show()