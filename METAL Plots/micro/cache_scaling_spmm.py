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
Speedup_16w =[3.02,16.08,36.42,37.21,37.93,39.31]
Speedup_32w =[5.06,20.01,37.82,70.21,71.26,73.21]
Speedup_64w=[9.61,18.92,40.21,102.62,108.1,109.66]
Speedup_128w=[17.26,32.17,41.61,109.19,118.36,127.21]
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
plt.savefig('Plots/pdfs/cache_scaling_spmm.pdf')
plt.show()