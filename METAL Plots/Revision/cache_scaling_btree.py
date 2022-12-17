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
Speedup_16w =[5.36,9.08,18.02,36.71,38.25,39.16]
Speedup_32w =[10.06,18.06,33.01,67.66,68.27,68.71]
Speedup_64w=[19.61,31.72,51.28,103.16,113.17,118.28]
Speedup_128w=[31.69,38.82,51.27,107.19,115.21,115.78]
fig,ax=plt.subplots(figsize=(7, 5.5))
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
plt.xlabel('Cache Size (in entries)',size=font, color='k')
plt.ylabel('Norm. Speed Up', size=font, color='k')
# plt.legend(["16 w","32 w","64 w","128w"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=4)
plt.savefig('Plots/pdfs/cache_scaling_btree.pdf')
plt.show()