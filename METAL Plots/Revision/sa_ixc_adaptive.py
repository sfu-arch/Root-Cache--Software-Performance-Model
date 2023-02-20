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

font = 32
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)


stream = []
metal = []
cache = []

font = 24

BM_name = ["B+Tree", "Hash", "SpMM","Analy.","RTree"]
opt = ([0.39, 0.53, 0.56, 0.37,0.92])#miss rate
cache = ([0.67, 0.85,  0.89,0.65, 0.92])
xcache = ([0.82, 0.91, 0.61, 0.84,  0.94])
metal = (([60.8, 57.3, 62.1, 69.8, 52.7]))
sway_cache = ([52.3,47.6,60.1,53,23.1])
eway_cache = ([41.7,33.6,57.6,48.9,21.3])
fway_cache = ([37.1,21.8,51.3,41.6,17.8])
eway_cache_vc = ([49.6,42.1,67.8,54.3,26.7])
sway_cache_vc = ([59.6,58.7,68.9,71.2,31.6])
eway_cache_adapt = ([53.2,51.7,60.03,61.7,13.6])
sway_cache_adapt = ([62.8,61.7,63.6,80.4,25.6])
vc_32_eway=([59.6,57.3,61.6,72.3,22.34])
vc_32_sway = ([65.7,64.38, 69.5,89.37,29.62])
# nrm = [3.8, 4, 5, 2, 6.5,6]

opt1=([])
cache1=([])
metal1=([])
xcache1=([])#hit rate
sway_cache1=([0,0,0,0,0])
eway_cache1=([0,0,0,0,0])
fway_cache1=([0,0,0,0,0])

X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))


# # nrm[i]=10-nrm[i]

for i in range(len(vc_32_sway)):
    fway_cache[i]=fway_cache[i]/metal[i]
    eway_cache[i]=eway_cache[i]/metal[i]
    sway_cache[i]=sway_cache[i]/metal[i]
    vc_32_sway[i]=vc_32_sway[i]/metal[i]
    vc_32_eway[i]=vc_32_eway[i]/metal[i]

fig, ax = plt.subplots(figsize=(22, 6))
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

# bar1 = plt.bar([i -0.108 for i in X_AXIS], [metal[i]for i, X in enumerate(metal)], width=0.1,  hatch="//", color="#e9e9e9")
# plt.bar([i - 0.02 for i in X_AXIS], [xcache[i] for i, X in enumerate(xcache)], hatch=".", width=0.1, color="gray")
plt.bar([i + 0.0 for i in X_AXIS], [(1/fway_cache[i])*1.96 for i, X in enumerate(fway_cache)], hatch="--", width=0.1, color="black")
# plt.bar([i + 0.21 for i in X_AXIS], [cache[i]for i, X in enumerate(metal)], width=0.1, color="#b1b1b1")
plt.bar([i + 0.11 for i in X_AXIS], [(1/eway_cache[i])*1.96 for i, X in enumerate(eway_cache)], width=0.1, color="grey")
plt.bar([i + 0.22 for i in X_AXIS], [(1/sway_cache[i])*1.96 for i, X in enumerate(sway_cache)], width=0.1,color="white",edgecolor="black")
plt.bar([i + 0.33 for i in X_AXIS], [(1/vc_32_eway[i])*1.96 for i, X in enumerate(vc_32_eway)], width=0.1,color="#b1b1b1",hatch="//")
plt.bar([i + 0.44 for i in X_AXIS], [(1/vc_32_sway[i])*1.96 for i, X in enumerate(vc_32_sway)], width=0.1,color="#c1c1c1",hatch="\\")


# plt.bar([i + 0.33 for i in X_AXIS], [(metal[i]/eway_cache_vc[i])/1.37 for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="\\\\", color="#b1b1b1")
# plt.bar([i + 0.44 for i in X_AXIS], [(metal[i]/sway_cache_vc[i])/1.37 for i,X in  enumerate(sway_cache_vc)], width=0.1, hatch="//", color="#c1c1c1")
# plt.bar([i + 0.55 for i in X_AXIS], [(metal[i]/eway_cache_adapt[i])/1.37 for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="--", color="#d1d1d1")
# plt.bar([i + 0.66 for i in X_AXIS], [(metal[i]/sway_cache_adapt[i])/1.37 for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="**", color="#e1e1e1")

# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=24, color="red", weight="bold")
#     k=k+1

legend = [ "4-way IXC", "8-way IXC", "16-way IXC","8-way ADA+VC", "16-way ADA+VC"]
plt.legend(legend, fontsize=18, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.92, 1.25), ncol=5)

plt.ylabel('Norm. Performance', size=font, color='k')
# plt.ylim(0, 3.0)


# plt.annotate("\nB+ Tree Search", (0.2, -0.2), xycoords='axes fraction',
#              textcoords='offset points', va='top', size=24, weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/sa_ixc_adaptive.pdf')
plt.show()
