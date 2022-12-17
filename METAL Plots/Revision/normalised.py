import sys

import math


import matplotlib.pyplot as plt
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

print(sys.path)

# from palettable.colorbrewer.sequential import YlGnBu_5

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

font = 24
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)




opt =[]
metal=[]
cache =[]

font = 16

BM_name = ["Rand. 100%", "Rand. 80%","Rand. 40%", "Hash", "SpMV", "SpMM"]
prefetch = [0.73, 2.68,3.01,0.67,3.41,3.97]
metal = [3.98,4.68,5.18,2.96,5.93,5.68]
opt = [1.13,2.21,1.73,1.31,2.33,2.87]

X_AXIS = np.linspace(-3,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(10, 4))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 20)
plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')


xticks_minor = [ 1.5 ]
ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.annotate("B+Tree Search",(0.12,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')



plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

plt.bar([i -0.5 for i in X_AXIS], [opt[i] for i,X in  enumerate(opt)], hatch = "--", width  = 0.5, color = "black")
plt.bar([i + 0.0 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(metal)], width  = 0.5, color = "#b1b1b1")
plt.bar([i +0.5 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], width  = 0.5,  hatch = "//", color = "#e9e9e9")

# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["OPT", "Preftech", "METAL"]
plt.legend(legend, fontsize=16, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1.0, 1.15),ncol = 3)

plt.ylabel('Norm. Speedup', size = font, color='k')
plt.ylim(0,7.0)


# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/normperf_extra.pdf')

