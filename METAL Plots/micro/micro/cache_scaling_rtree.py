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

font = 24

# Fixing random state for reproducibility
# np.random.seed(19680801)

x_pos = [0,1,5,8,9]
cache =['8','16','32','64','128','256']
Speedup_16w =[2.71,4.32,9.66,19.23,41.26,41.16]
Speedup_32w =[4.62,9.31,18.11,37.01,62.13,121.21]
Speedup_64w=[8.31,16.62,33.11,67.31,121.61,193.17]
Speedup_128w=[15.31,31.71,62.45,114.35,178.61,217.58]
fig,ax=plt.subplots(figsize=(9, 7))
ax.set_facecolor('w')
ax.set_axisbelow(True)
scaling=[1.12,1.18,1.16,1.21]
for i in range(len(Speedup_16w)):
    Speedup_16w[i]=Speedup_16w[i]/scaling[0]
    Speedup_32w[i]=Speedup_32w[i]/scaling[1]
    Speedup_64w[i]=Speedup_64w[i]/scaling[2]
    Speedup_128w[i]=Speedup_128w[i]/scaling[3]
plt.scatter(cache, Speedup_16w, marker='+',s=130,facecolor="black",linewidths=2)
plt.scatter(cache, Speedup_32w, marker='^',s=130,edgecolors="black",facecolors="none",linewidths=2)
plt.scatter(cache, Speedup_64w, marker='o',s=130,edgecolors="black",facecolors="none",linewidths=2)
plt.scatter(cache, Speedup_128w, marker='s',s=130,edgecolors="black",facecolors="none",linewidths=2)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')
# plt.ylim(0,120)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
plt.xlabel('Cache Size (in kB)',size=font, color='k')
#plt.ylabel('Norm. Speed Up', size=font, color='k')
# plt.legend(["16 w","32 w","64 w","128w"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=4)
plt.savefig('Plots/pdfs/cache_scaling_rtree.pdf')
# plt.show()