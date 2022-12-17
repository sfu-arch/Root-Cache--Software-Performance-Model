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
Speedup_16w =[4.27,8.06,15.42,32.81,33.266,33.29]
Speedup_32w =[9.63,18.21,32.77,66.26,69.31,71]
Speedup_64w=[18.28,33.17,52.62,106.13,118.24,121.36]
Speedup_128w=[32.17,37.64,64.88,107.18,118.62,126.10]
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
plt.xlabel('Cache Size (in kB)',size=font, color='k')
plt.ylabel('Norm. Speed Up', size=font, color='k')
# plt.legend(["16 w","32 w","64 w","128w"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=4)
plt.savefig('Plots/pdfs/cache_scaling_hash.pdf')
plt.show()