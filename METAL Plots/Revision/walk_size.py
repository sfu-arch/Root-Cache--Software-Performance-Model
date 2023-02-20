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
cache = ([2.37, 1.82, 2.4, 8.21, 9.26])
metal = (([6.08, 5.73, 8.21, 3.02, 5.27]))
fa_16 = ([0,0,0,0,0])
fa_8=([0,0,0,0,0])
fa_4=([0,0,0,0,0])
eway_32 = ([0,0,0,0,0])
eway_16=([0,0,0,0,0])
eway_8=([0,0,0,0,0])
# nrm = [5, 2, 6.5,6,4.72,3.87,5.06,3.21]

cache1=([0,0,0,0,0])
sway_cache1=([0,0,0,0,0])
eway_cache1=([0,0,0,0,0])
fa_161=([0,0,0,0,0])
fa_81=([0,0,0,0,0])
fa_41=([0,0,0,0,0])
eway_321 = ([0,0,0,0,0])
eway_161=([0,0,0,0,0])
eway_81=([0,0,0,0,0])
metal1=([0,0,0,0,0])

for i in range(3):
    fa_161[i]=(10-cache[i])/1.72
    fa_81[i]=(10-cache[i])/1.44
    fa_41[i]=(10-cache[i])/1.21
    eway_321[i]=(10-cache[i])/1.48
    eway_161[i]=(10-cache[i])/1.13
    eway_81[i]=(10-cache[i])/0.96
    cache1[i]=10-cache[i]
    metal1[i]=10-metal[i]


for i in range(3,5):
    fa_161[i]=(cache[i])/1.72
    fa_81[i]=(cache[i])/1.44
    fa_41[i]=(cache[i])/1.21
    eway_321[i]=(cache[i])/1.48
    eway_161[i]=(cache[i])/1.13
    eway_81[i]=(cache[i])/0.96
    cache1[i]=cache[i]
    metal1[i]=metal[i]

for i in range(5):
    fa_16[i]=cache[i]*0.4*1.72+fa_161[i]*100
    fa_8[i]=cache[i]*0.4*1.44+fa_81[i]*100
    fa_4[i]=cache[i]*0.4*1.21+fa_41[i]*100
    eway_32[i]=cache[i]*0.4*1.48+eway_321[i]*100
    eway_16[i]=cache[i]*0.4*1.13+eway_161[i]*100
    eway_8[i]=cache[i]*0.4*0.96+eway_81[i]*100
    cache[i]=cache[i]*0.4 + cache1[i]*100
    metal[i]=metal[i]*1+metal1[i]*100

X_AXIS = np.linspace(1.5,len(BM_name),len(BM_name))

print(sway_cache1)
print(cache1)

fig,ax=plt.subplots(figsize=(21.5, 6))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS ,ha= 'center', color='k') #rotation
ax.set_xticks([1.75,2.6,3.5,4.4,5.3])
ax.set_xticklabels(BM_name)
plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')


xticks_minor = [ 0 ]
# ax.set_xticks( xticks_minor, minor=False )

# ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )

plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)





# bar1 = plt.bar([i -0.104 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], width  = 0.1,  hatch = "//", color = "#e9e9e9")
# plt.bar([i +0.0 for i in X_AXIS], [xcache[i] for i,X in  enumerate(xcache)], hatch = ".",width  = 0.1, color = "gray")
# plt.bar([i +0.102 for i in X_AXIS], [opt[i] for i,X in  enumerate(opt)], hatch = "--", width  = 0.1, color = "black")
# plt.bar([i + 0.21 for i in X_AXIS], [cache[i] for i,X in  enumerate(metal)], width  = 0.1, color = "#b1b1b1")
# plt.bar([i +0.315 for i in X_AXIS], [prefetch[i] for i,X in  enumerate(prefetch)], hatch = "--",edgecolor="black",width  = 0.1, color = "white")
# plt.bar([i +0.425 for i in X_AXIS], [sway_cache[i] for i,X in  enumerate(sway_cache)], hatch = "\\\\",edgecolor="black",width  = 0.1, color = "#c1c1c1")
# plt.bar([i +0.535 for i in X_AXIS], [eway_cache[i] for i,X in  enumerate(eway_cache)], hatch = "--",edgecolor="black",width  = 0.1, color = "#d1d1d1")

plt.bar([i -0.11 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], width  = 0.1,  hatch = "//", color = "#e9e9e9",align='center')
plt.bar([i +0.0 for i in X_AXIS], [fa_16[i] for i,X in  enumerate(fa_16)], width  = 0.1,  color = "white",align='center',edgecolor="black",linewidth=2)
plt.bar([i +0.108 for i in X_AXIS], [fa_8[i] for i,X in  enumerate(fa_8)], hatch = "--", width  = 0.1, color = "black",align='center')
plt.bar([i + 0.21 for i in X_AXIS], [fa_4[i] for i,X in  enumerate(fa_4)], width  = 0.1, color = "#b1b1b1",align='center')
plt.bar([i +0.315 for i in X_AXIS], [eway_32[i] for i,X in  enumerate(eway_32)], hatch = "--",edgecolor="black",width  = 0.1, color = "white",align='center',linewidth=2)
plt.bar([i +0.425 for i in X_AXIS], [eway_16[i] for i,X in  enumerate(eway_16)], hatch = "-",width  = 0.1, color = "black",align='center',edgecolor="white",linewidth=2)
plt.bar([i +0.535 for i in X_AXIS], [eway_8[i] for i,X in  enumerate(eway_8)], hatch = "--",width  = 0.1, color = "#b1b1b1",align='center')



# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)

# k=0
# for i in bar1:
#     height = i.get_height()
#     plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=14, color="red", weight="bold")
#     k=k+1
# summ=0
# for i in range(len(cache)):
#     summ = summ + (prefetch[i]/metal[i])
# print()
# print()
# avg=(summ)/(5)
# print("avg is",avg)

legend = ["METAL","FA-Addr(16x)","FA-Addr(8x)","FA-Addr(4x)","8-way(32x)", "8-way(16x)","8-way(8x)"]
plt.legend(legend, fontsize=18,loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.99, 1.2),ncol=7)

plt.ylabel('Walk Latency (cycles)', size = font, color='k')
# plt.ylim(0,10.0)



# plt.annotate("\nB+ Tree Search",(0.2,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = 24 ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/walklatency_timesplot.pdf')
plt.show()

