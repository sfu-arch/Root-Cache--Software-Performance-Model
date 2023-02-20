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


stream = []
metal = []
cache = []

font = 24

BM_name = ["B+Tree", "Hash", "SpMM","Analy.","RTree"]
opt = ([0.12, 0.28, 0.03, 0.16,0.19])
metal = ([0.62, 0.68,  0.28,0.55, 0.48])
# cache = ([0.61, 0.70,  0.45,0.57, 0.63])
# nrm = [3.8, 4, 5, 2, 6.5,6]

X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))

# for i in range(6):
#     opt[i]=10-opt[i]
# prefetch[i]=10-prefetch[i]
# cache[i]=10-cache[i]
# metal[i]=10-metal[i]
# xcache[i]=10-xcache[i]
# # nrm[i]=10-nrm[i]
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS, ha='center', color='k', rotation=20)
plt.xticks(size=font, va="top")
plt.yticks(fontsize=font, color='k')


xticks_minor = [0]
ax.set_xticks(xticks_minor, minor=True)

ax.tick_params(axis='x', which='minor', direction='out', length=40, width=3)

plt.yticks(fontsize=font, color='k')

ax.set_xticklabels(BM_name)



# plt.bar([i +0.15 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "//",width  = 0.15, color = "#c5c5c5")

# plt.bar([i - 0.22 for i in X_AXIS], [cache[i]*100 for i,X in  enumerate(cache)], hatch = ".", width  = 0.2, color = "#b1b1b1")
bar1 = plt.bar([i - 0.01 for i in X_AXIS], [metal[i]*100 for i, X in enumerate(metal)], width=0.35,  hatch="//", color="#e9e9e9")
plt.bar([i + 0.35 for i in X_AXIS], [opt[i]*100 for i, X in enumerate(opt)], hatch="--", width=0.35, color="black")

# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=24, color="red", weight="bold")
#     k=k+1

legend = [ "METAL","METAL OPT"]
plt.legend(legend, fontsize=18, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.6, 1.1), ncol=4)

plt.ylabel('Wasted Entries %', size=font, color='k')
plt.ylim(0, 100.0)


# plt.annotate("\nB+ Tree Search", (0.2, -0.2), xycoords='axes fraction',
#              textcoords='offset points', va='top', size=24, weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/metal_Wasted.pdf')
plt.show()
