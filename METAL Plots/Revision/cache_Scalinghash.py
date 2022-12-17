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
walkers = ['128','256','512','1024','2048','4196']
Speedup_16w = [1.03,1.91,2.07,3.82,4.96,5.01]
Speedup_32w = [1.23,2.17,2.93,6.01,7.13,9.67]
Speedup_64w=[1.6,2.7,3.48,7.13,11.34,12.77]
fig,ax=plt.subplots(figsize=(7, 5.5))
ax.set_facecolor('w')
ax.set_axisbelow(True)

plt.scatter(walkers, Speedup_16w, marker='^',s=80)
plt.scatter(walkers, Speedup_32w, marker='o',s=80)
plt.scatter(walkers, Speedup_64w, marker='+',s=80)

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
plt.legend(["16 w","32 w","64 w"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=3)
plt.savefig('Plots/pdfs/cache_scalinghash.pdf')
plt.show()