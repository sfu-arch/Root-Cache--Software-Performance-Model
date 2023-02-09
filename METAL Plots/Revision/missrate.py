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
opt = ([0.39, 0.53, 0.56, 0.37,0.92])
cache = ([0.67, 0.85,  0.89,0.65, 0.92])
metal = (([0.03, 0.23, 0.01,0.08, 0.42]))
xcache = ([0.82, 0.91, 0.61, 0.84,  0.94])
sway_cache = ([0,0,0,0,0])
eway_cache = ([0,0,0,0,0])

for i in range(5):
	sway_cache[i]=cache[i]*1.2
	eway_cache[i]=cache[i]*1.09
	if(sway_cache[i]>=1):
		sway_cache[i]=0.9999
	if(eway_cache[i]>=1):
		eway_cache[i]=0.9999
	
	

# nrm = [3.8, 4, 5, 2, 6.5,6]

X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))

# for i in range(6):
#     opt[i]=10-opt[i]
# prefetch[i]=10-prefetch[i]
# cache[i]=10-cache[i]
# metal[i]=10-metal[i]
# xcache[i]=10-xcache[i]
# # nrm[i]=10-nrm[i]
fig, ax = plt.subplots(figsize=(20, 6))
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

ax.tick_params(axis='x', which='minor', direction='out', length=60, width=3)

plt.yticks(fontsize=font, color='k')

ax.set_xticklabels(BM_name)



# plt.bar([i +0.15 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "//",width  = 0.15, color = "#c5c5c5")

bar1 = plt.bar([i -0.108 for i in X_AXIS], [metal[i]for i, X in enumerate(metal)], width=0.1,  hatch="//", color="#e9e9e9")
plt.bar([i - 0.00 for i in X_AXIS], [xcache[i] for i, X in enumerate(xcache)], hatch=".", width=0.1, color="gray")
plt.bar([i + 0.103 for i in X_AXIS], [opt[i]for i, X in enumerate(opt)], hatch="--", width=0.1, color="black")
plt.bar([i + 0.21 for i in X_AXIS], [cache[i]for i, X in enumerate(metal)], width=0.1, color="#b1b1b1")
plt.bar([i + 0.315 for i in X_AXIS], [eway_cache[i]for i, X in enumerate(eway_cache)], width=0.1, color="#d1d1d1", hatch="-")
plt.bar([i + 0.42 for i in X_AXIS], [sway_cache[i]for i, X in enumerate(sway_cache)], width=0.10, color="#c1c1c1", hatch="\\")
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=24, color="red", weight="bold")
#     k=k+1

legend = [ "METAL","X-Cache", "FA-Addr(OPT)", "FA-Addr", "Ideal 8-way" , "Ideal 16-way"]
plt.legend(legend, fontsize=18, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.99, 1.2), ncol=6)

plt.ylabel('Miss rate', size=font, color='k')
plt.ylim(0, 1.0)


# plt.annotate("\nB+ Tree Search", (0.2, -0.2), xycoords='axes fraction',
#              textcoords='offset points', va='top', size=24, weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/missrate.pdf')
plt.show()
