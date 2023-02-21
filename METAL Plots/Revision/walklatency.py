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




stream =[]
metal=[]
cache =[]

font = 24

BM_name = ["B+Tree", "Hash","SpMM","Analy.", "RTree"]
opt = ([3.84, 2.16, 4.43,7.16, 8.34])
prefetch = ([4.6, 1.92, 5.0, 6.63, 8.02])
cache = ([2.37, 1.82, 2.4, 8.21, 9.26])
metal = (([6.08, 5.73, 6.21, 3.02, 5.27]))
xcache = ([3.98, 1.77,4.87, 6.03, 7.86])
# nrm = [5, 2, 6.5,6,4.72,3.87,5.06,3.21]


for i in range(3):
    opt[i]=10-opt[i]
    prefetch[i]=10-prefetch[i]
    cache[i]=10-cache[i]
    metal[i]=10-metal[i]
    xcache[i]=10-xcache[i]

for i in range(5):
	opt[i]=opt[i]*0.9
	prefetch[i]=prefetch[i]*0.9
	cache[i]=cache[i]*0.9

X_AXIS = np.linspace(1.5,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(18, 6))
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


xticks_minor = [ 0 ]
# ax.set_xticks( xticks_minor, minor=False )

# ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )

plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)





bar1 = plt.bar([i -0.154 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], width  = 0.15,  hatch = "//", color = "#e9e9e9")
plt.bar([i +0.0 for i in X_AXIS], [xcache[i] for i,X in  enumerate(xcache)], hatch = ".",width  = 0.15, color = "gray")
plt.bar([i +0.152 for i in X_AXIS], [opt[i] for i,X in  enumerate(opt)], hatch = "--", width  = 0.15, color = "black")
plt.bar([i + 0.31 for i in X_AXIS], [cache[i] for i,X in  enumerate(metal)], width  = 0.15, color = "#b1b1b1")
plt.bar([i +0.465 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "--",edgecolor="black",width  = 0.15, color = "white")
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=14, color="red", weight="bold")
#     k=k+1
summ=0
for i in range(len(cache)):
    summ = summ + (prefetch[i]/metal[i])
print()
print()
avg=(summ)/(5)
print("avg is",avg)

legend = ["METAL","X-Cache","FA-Addr(OPT)","FA-Addr", "Prefetch"]
plt.legend(legend, fontsize=18,loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 1.2),ncol=5)

plt.ylabel('Walk Latency', size = font, color='k')
plt.ylim(0,10.0)



# plt.annotate("\nB+ Tree Search",(0.2,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = 24 ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/walklatency.pdf')
plt.show()


