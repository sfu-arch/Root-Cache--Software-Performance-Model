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
walkers = ['8','16','32','64','128','256']
Speedup_Random = [2.07,4.18,9.32,15.41,19.36,21.24]
Speedup_80 = [2.33,4.61,9.73,17.22,19.46,21.93]
Speedup_40=[2.57,5.48,11.21,18.76,22.73,24.86]
Speedup_Hash =[1.61,3.87,6.01,7.13,7.54,7.59]
Speedup_SpMM = [2.87, 5.18, 8.33, 12.46, 15.51, 16.15]
Speedup_SpMv = [3.01, 5.96, 7.34, 9.27, 11.18, 13.55]
fig,ax=plt.subplots(figsize=(7, 6))
ax.set_facecolor('w')
ax.set_axisbelow(True)

plt.scatter(walkers, Speedup_Random, marker='^',s=80)
plt.scatter(walkers, Speedup_80, marker='o',s=80)
plt.scatter(walkers, Speedup_40, marker='+',s=80)
plt.scatter(walkers, Speedup_Hash, marker='v',s=80)
plt.scatter(walkers, Speedup_SpMM, marker='*',s=80)
plt.scatter(walkers, Speedup_SpMv, marker='s',s=80)
# plt.xticks(x_pos, walkers)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')

ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
plt.xlabel('No. of walkers',size=font, color='k')
plt.ylabel('Norm. Speed Up', size=font, color='k')
plt.legend(["Rand. 100%","Rand. 80%","Rand. 40%", "Hash","SpMM","SpMV"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.20000002),ncol=3)
plt.savefig('Plots/pdfs/walkerscale_cloud.pdf')
plt.show()