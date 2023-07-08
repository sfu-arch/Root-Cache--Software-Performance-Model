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

font = 36

BM_name = ["Scan", "JOIN", "RTree","SpMM","KV-Store"]
# opt = ([0.39, 0.53, 0.56, 0.37,0.92])#miss rate
# cache = ([0.67, 0.85,  0.89,0.65, 0.92])
# metal = (([0.03, 0.23, 0.01,0.08, 0.42]))
# xcache = ([0.82, 0.91, 0.61, 0.84,  0.94])
opt = (	[0.39,	0.37,	0.92,	0.56,	0.53]	)
cache = (	[0.67,	0.65,	0.92	,0.89,	0.85]	)
metal = (([	0.03,	0.08,	0.42,	0.01	,0.23]	))
metal_ix = (([	0.18,	0.22,	0.63,	0.04	,0.37]	))
xcache = ([	0.82,	0.84,	0.94,	0.61	,0.91]	)
sway_cache = ([0,0,0,0,0])
eway_cache = ([0,0,0,0,0])
# nrm = [3.8, 4, 5, 2, 6.5,6]

opt1=([])
cache1=([])
metal1=([])
xcache1=([])#hit rate
sway_cache1=([0,0,0,0,0])
eway_cache1=([0,0,0,0,0])

X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))

for i in range(5):
    sway_cache[i]=cache[i]/1.72
    eway_cache[i]=cache[i]/1.48
# # nrm[i]=10-nrm[i]

# for i in range(len(opt)):
#     opt[i]=opt[i]*100
#     cache[i]=cache[i]*100
#     metal[i]=metal[i]*100
#     xcache[i]=xcache[i]*100

fig, ax = plt.subplots(figsize=(16, 8.8))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS, ha='center', color='k', rotation=0)
plt.xticks(size=font, va="top")
plt.yticks(fontsize=font, color='k')


xticks_minor = [2.8,3.7,4.6]
ax.set_xticks(xticks_minor, minor=True)

ax.tick_params(axis='x', which='minor', direction='out', length=40, width=3)

plt.yticks(fontsize=font, color='k')

ax.set_xticklabels(BM_name)



# plt.bar([i +0.15 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "//",width  = 0.15, color = "#c5c5c5")
bar5=plt.bar([i - 0.3 for i in X_AXIS], [metal_ix[i]for i, X in enumerate(metal_ix)], width=0.15, color="#c9c9c9")
bar1 = plt.bar([i -0.15 for i in X_AXIS], [metal[i]for i, X in enumerate(metal)], width=0.15,  hatch="//", color="#e9e9e9")
bar4=plt.bar([i - 0.0 for i in X_AXIS], [cache[i] for i, X in enumerate(cache)], hatch="\\\\", width=0.15, color="grey")
bar3=plt.bar([i + 0.15 for i in X_AXIS], [xcache[i]for i, X in enumerate(xcache)], width=0.15, color="#b1b1b1")
bar2=plt.bar([i + 0.3 for i in X_AXIS], [opt[i]for i, X in enumerate(opt)], width=0.15, color="black")

# plt.bar([i + 0.32 for i in X_AXIS], [sway_cache[i]for i, X in enumerate(sway_cache)], width=0.1, hatch="\\\\", color="#c1c1c1")
# plt.bar([i + 0.43 for i in X_AXIS], [eway_cache[i]for i, X in enumerate(eway_cache)], width=0.1, hatch="--",color="#d1d1d1")
# # plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=24, color="red", weight="bold")
#     k=k+1
nrmmetalix=[43,52,62,24,68]
nrmmetal=[20,30,44,16.7,50]
nrmxcache=[73,71,91,43,87]
nrmopt=[92,86,94,87,92]
nrmaddr=[100,100,100,100,100]
font1=32
k=0
for i in bar5:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrmmetalix[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold",rotation=90)
    k=k+1
k=0
for i in bar1:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrmmetal[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold",rotation=90)
    k=k+1
k=0
for i in bar3:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrmxcache[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold",rotation=90)
    k=k+1
k=0
for i in bar2:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrmopt[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold",rotation=90)
    k=k+1
k=0
for i in bar4:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrmaddr[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold",rotation=90)
    k=k+1
legend = ["METAL-IX", "METAL", "FA","X-Cache", "FA-OPT",  "FA-Addr(16x)", "Ideal 16-way(32x)"]
plt.legend(legend, fontsize=30, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.95, 1.45), ncol=3)

plt.ylabel('Miss rate', size=font, color='k')
plt.ylim(0, 1.0)

ax.axvline(x=5.44, color='red',linewidth=4)
ax.text(5.465, 0.22, 'Working Set%', rotation=90, color='red',size=32,weight="bold")
plt.annotate("Gorgon", (0.16, -0.1), xycoords='axes fraction',
             textcoords='offset points', va='top', size=font, weight='bold')
plt.annotate("Aurochs",   (0.41,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Capstan",   (0.61,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("WidX",   (0.82,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('pdfs/missrate2.pdf')
# plt.show()