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
from matplotlib.ticker import FuncFormatter
import csv
import matplotlib.ticker as mticker


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

# font = 24

# BM_name = ["B+Tree", "Hash", "SpMM","JOIN","RTree"]
# opt = ([0.39, 0.53, 0.56, 0.37,0.92])#miss rate
# cache = ([0.67, 0.85,  0.89,0.65, 0.92])
# xcache = ([0.82, 0.91, 0.61, 0.84,  0.94])
# metal = (([60.8, 57.3, 62.1, 69.8, 52.7]))
# sway_cache = ([52.3,47.6,60.1,53,23.1])
# eway_cache = ([41.7,33.6,57.6,48.9,21.3])
# fway_cache = ([37.1,21.8,51.3,41.6,17.8])
# eway_cache_vc = ([49.6,42.1,59.8,54.3,26.7])
# sway_cache_vc = ([59.6,58.7,61.9,71.2,31.6])
# eway_cache_adapt = ([53.2,51.7,60.03,61.7,13.6])
# sway_cache_adapt = ([62.8,61.7,63.6,80.4,25.6])
# vc_e = ([42.6,37.4,58.1,49.7,22.7])
# vc_s = ([54.3,50.7,60.8,54.8,28.9])
BM_name =	["Scan",	"JOIN",	"RTree",	"SpMM",	"KVStore"]	
opt = ([	0.39,	0.37	,0.92,	0.56	,0.53	])#miss rate
cache = (	[0.67,	0.65,	0.92,	0.89	,0.85	])
xcache = ([	0.82,	0.84,	0.94,0.61	,0.91	])
metal = ((	[60.8,	69.8,	52.7	,62.1,	57.3]	))
sway_cache = (	[52.3,	53,	23.1,	60.1	,47.6]	)
eway_cache = ([	41.7	,48.9,	21.3,	57.6,	33.6]	)
fway_cache = (	[37.1,	41.6	,17.8,	51.3,	21.8]	)
eway_cache_vc = (	[49.6,	54.3	,26.7	,59.8,	42.1]	)
sway_cache_vc = (	[59.6,	71.2,	31.6,	61.9	,58.7]	)
eway_cache_adapt = (	[53.2	,61.7,	13.6,	60.03,	51.7]	)
sway_cache_adapt = (	[62.8,	80.4,	25.6	,63.6	,61.7]	)
vc_e = (	[42.6,	49.7,	22.7,	58.1,	37.4]	)
vc_s = (	[54.3	,54.8,	28.9,	60.8	,50.7]	)
# nrm = [3.8, 4, 5, 2, 6.5,6]

opt1=([])
cache1=([])
metal1=([])
xcache1=([])#hit rate
sway_cache1=([0,0,0,0,0])
eway_cache1=([0,0,0,0,0])
fway_cache1=([0,0,0,0,0])

# metal_mr = ([0.03, 0.23, 0.01,0.08, 0.26])
# sway_cache_mr = ([0.26,0.29,0.16,0.22,0.39])
# eway_cache_mr = ([0.31,0.4,0.21,0.29,0.41])
# fway_cache_mr = ([0.35,0.41,0.27,0.31,0.45])
# sway_vc_mr= ([0.21,0.23,0.09,0.17,0.32])
# vc_s_mr= ([0.23,0.25,0.13,0.21,0.34])

	
sway_cache_mr = (	[0.26,	0.22,	0.39,	0.16,	0.29]	)
eway_cache_mr = (	[0.31,	0.29,	0.41,	0.21,	0.4	])
fway_cache_mr = (	[0.35,	0.31,	0.45,	0.27,	0.41]	)
sway_vc_mr= (	[0.21,	0.17	,0.32,	0.09,	0.23]	)
vc_s_mr= (	[0.23,	0.21,	0.34,	0.13	,0.25]	)

X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))


# # nrm[i]=10-nrm[i]

for i in range(len(fway_cache)):
    fway_cache[i]=fway_cache[i]/metal[i]
    eway_cache[i]=eway_cache[i]/metal[i]
    sway_cache[i]=sway_cache[i]/metal[i]

fig, ax = plt.subplots(figsize=(14, 6))


ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='gray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS, ha='center', color='k')
ax.set_xticks([1.75,2.6,3.5,4.4,5.3])
ax.set_xticklabels(BM_name)
plt.xticks(size=font, va="top")
plt.yticks(fontsize=font, color='k')


xticks_minor = [3.1,3.9,4.8]
ax.set_xticks(xticks_minor, minor=True)

ax.tick_params(axis='x', which='minor', direction='out', length=40, width=3)

# plt.yticks(fontsize=font, color='k')
ax2 = ax.twinx()
# ax.set_yticks((0.6,1.2,1.8,2.4,3),fontsize=font, color='k')
# ax2.set_yticks((0.2,0.4,0.6,0.8,1),fontsize=font, color='red')
# ax2.tick_params(axis='y', labelcolor="red")


ax.set_xticklabels(BM_name)
# ax2.set_yticks(fontsize=font, color='red')
plt.gca().yaxis.grid(False)

# def y_fmt(x, y):
#     return '{:.1f}'.format(y)

# ax2.yaxis.set_major_formatter(FuncFormatter(y_fmt))



# plt.bar([i +0.15 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "//",width  = 0.15, color = "#c5c5c5")

# bar1 = plt.bar([i -0.108 for i in X_AXIS], [metal[i]for i, X in enumerate(metal)], width=0.1,  hatch="//", color="#e9e9e9")
# plt.bar([i - 0.02 for i in X_AXIS], [xcache[i] for i, X in enumerate(xcache)], hatch=".", width=0.1, color="gray")
ax.bar([i + 0.0 for i in X_AXIS], [1/fway_cache[i]for i, X in enumerate(fway_cache)], hatch="--", width=0.12, color="black")
# plt.bar([i + 0.11 for i in X_AXIS], [cache[i]for i, X in enumerate(metal)], width=0.1, color="#b1b1b1")
ax.bar([i + 0.13 for i in X_AXIS], [1/eway_cache[i]for i, X in enumerate(eway_cache)], width=0.12, color="grey")
ax.bar([i + 0.26 for i in X_AXIS], [1/sway_cache[i]for i, X in enumerate(sway_cache)], width=0.12,color="white",edgecolor="black")
# plt.bar([i + 0.18 for i in X_AXIS], [metal[i]/eway_cache_vc[i] for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="\\\\", color="#b1b1b1")
ax.bar([i + 0.39 for i in X_AXIS], [metal[i]/sway_cache_vc[i] for i,X in  enumerate(sway_cache_vc)], width=0.12, hatch="//", color="#c1c1c1")
# plt.bar([i + 0.30 for i in X_AXIS], [metal[i]/eway_cache_adapt[i] for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="--", color="#d1d1d1")
# plt.bar([i + 0.36 for i in X_AXIS], [metal[i]/sway_cache_adapt[i] for i,X in  enumerate(eway_cache_vc)], width=0.1, hatch="**", color="#e1e1e1")
# plt.bar([i + 0.42 for i in X_AXIS], [metal[i]/vc_e[i] for i,X in  enumerate(vc_e)], width=0.1, hatch="/", color="#e1e1e1")
ax.bar([i + 0.52 for i in X_AXIS], [metal[i]/vc_s[i] for i,X in  enumerate(vc_s)], width=0.12, hatch="\\", color="#e1e1e1")
ax2.plot([i + 0.0 for i in X_AXIS], fway_cache_mr, 'r',marker="o",linestyle="none",markersize=10)
ax2.plot([i + 0.13 for i in X_AXIS], eway_cache_mr, 'r',marker="o",linestyle="none",markersize=10)
ax2.plot([i + 0.26 for i in X_AXIS], sway_cache_mr, 'r',marker="o",linestyle="none",markersize=10)
ax2.plot([i + 0.39 for i in X_AXIS], sway_vc_mr, 'r',marker="o",linestyle="none",markersize=10)
ax2.plot([i + 0.52 for i in X_AXIS], vc_s_mr, 'r',marker="o",linestyle="none",markersize=10)
# plt.bar([i + 0.1 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.1, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.15 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.1, color = "#D3D3D3", height=1.6)


# Apply the formatter to the y-axis

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=24, color="red", weight="bold")
#     k=k+1

legend = ["4-way", "8-way", "16-way", "16-way VC32","16-way VC16"]
ax.legend(legend, fontsize=26, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1.14,1.255), ncol=6,handletextpad=0.05,columnspacing=0.39)
label1=ax2.set_ylabel('Miss Rate', color='r',fontsize=32)
ax2.yaxis.set_tick_params(labelsize=30,labelcolor="r")
ax.set_ylabel('Norm. Latency', size=font, color='k')
# ax2.tick_params(axis='y', which='minor', left=False)
# plt.ylim(0, 3.0)
ax2.set_ylim(0,1)
y_step = 0.5
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_step))
formatter = mticker.FuncFormatter(lambda x, _: '0' if x == 0 else f'{x:.1f}'.lstrip('0'))
ax2.yaxis.set_major_formatter(formatter)

# ax2.set_yticks[0].label1.set_visible(False)
font=24
plt.annotate("Gorgon", (0.15, -0.13), xycoords='axes fraction',
             textcoords='offset points', va='top', size=font, weight='bold')
plt.annotate("Aurochs",   (0.42,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Capstan",   (0.599,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("WidX",   (0.82,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/sa_ixc.pdf')
# plt.show()