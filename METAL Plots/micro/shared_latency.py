import sys

import math


import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
from statistics import mean
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

font = 36
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)




stream =[]
metal=[]
cache =[]

font = 38

# BM_name = ['B+Tree' , "Hash", "SpMV","JOIN","SpMM"]
# cache = ([30*9000/9000, 25*9000/9000,42*9000/9000,16*9000/9000,40*9000/9000])
# assoc16 = ([30*7000/9000, 25*7000/9000,42*7000/9000, 16*7000/9000,40*7000/9000])#16way
# xcache=([1.11*7000/9000,1.52*7/9,1.31*7/9,1.62*7/9,1.44*7/9])
# BM_name = ['B+Tree' ,"Hash", "SpMV","JOIN","RTree"]
# cache = ([ 30*9000/9000,25*9000/9000,42*9000/9000,16*9000/9000,57*9000/9000])
# assoc16 = ([ 30*9000/9000,25*7000/9000,42*7000/9000, 16*7000/9000,57*7000/9000])#16way
# xcache=([1.11*7000/9000,1.52*7/9,1.31*7/9,1.62*7/9,4.12*7/9])
BM_name =	["B+Tree",	"KVStore"	,"JOIN",	"SpMM",	"RTree"]
# c128 = (	[1.19,	1.36	,1.28,1.06,1.47])
# c64 = (	[1.37,1.57,1.46,1.11,1.59])
# c32=(	[1.44,1.78,1.63,1.25,1.94])
# BM_name =	["B+Tree",	"KVStore"	,"JOIN",	"SpMM",	"RTree"]
# c128 = (	[0.22,	0.36	,0.28,0.06,0.47])
# c64 = (	[0.4,0.57,0.46,0.11,0.59])
# c32=(	[0.47,0.78,0.63,0.25,0.94])
# nrm128 = [79,63,73,91,58]
# nrm64=[66,61,64,86,47]
# nrm32=[59,44,51,79,38]

BM_name =	["Scan", "JOIN"	,"RTree",	"SpMM",	"KVStore"	]
c128 = 	[0.22,	0.28,	0.47,	0.06,	0.36]	
c64 = [	0.4	,0.46,	0.59,	0.11	,0.57	]
c32=	[0.47,	0.63,	0.94	,0.25,	0.78]	

print("128, 64, 32")
print(mean(c128),mean(c64),mean(c32))
c128 = (	[0.22,	0.28,	0.47,	0.06,	0.36]	)
c64 = ([	0.4	,0.46,	0.59,	0.11	,0.57	])
c32=(	[0.47,	0.63,	0.94	,0.25,	0.78]	)
nrm128 =	([79	,73,	58,	91	,63	])
nrm64=	([66,64,	47,	86,	61	])
nrm32=(	[59,	51,	38,	79	,44	])
# c256 = ([1,1,1,1,1])
# for i in range(len((assoc16))):
#     cache[i]=cache[i]/8
#     assoc16[i]=assoc16[i]/8

# for i in range(len(assoc16)):
#     # metal[i]=metal[i]/cache[i]
#     # assoc16[i]=assoc16[i]/cache[i]
#     # xcache[i]=xcache[i]/cache[i]
#     # cache[i]=cache[i]/cache[i]
#     metal[i]=metal[i]/assoc16[i]
    
#     xcache[i]=xcache[i]/assoc16[i]
#     assoc16[i]=assoc16[i]/assoc16[i]
#     # cache[i]=cache[i]/assoc16[i]
    
    
nrm128 = [79,63,73,91,58]
nrm64=[66,61,64,86,47]
nrm32=[59,44,51,79,38]

X_AXIS = np.linspace(3,len(BM_name),len(BM_name))



fig,ax=plt.subplots(figsize=(17, 8.4))
ax.set_facecolor('w')
ax.set_axisbelow(True)
# ax.spines['bottom'].set_color('k')
# ax.spines['bottom'].set_color('k')
ax.spines['left'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 0)
plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')


xticks_minor = [3.7,4.2,4.7]
ax.set_xticks(xticks_minor, minor=True)

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)
# ax.hlines(y=0, xmin=4, xmax=20, linewidth=6, color='r')
plt.axhline(y=0, color='black',linewidth=8)
# plt.bar([i - 0.20 for i in X_AXIS], [stream[i]/X for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")
# plt.bar([i - 0.201 for i in X_AXIS], [c256[i] for i,X in  enumerate(c256)], hatch = "", width  = 0.1, color = "black")
bar1 = plt.bar([i - 0.1 for i in X_AXIS], [c128[i]*100 for i,X in  enumerate(c128)], hatch = "//", width  = 0.1, color = "#b1b1b1")
bar2=plt.bar([i + 0.005 for i in X_AXIS], [c64[i]*100 for i,X in  enumerate(c64)], hatch = "", width  = 0.1, color = "#d1d1d1")
bar3=plt.bar([i + 0.108 for i in X_AXIS], [c32[i]*100 for i,X in  enumerate(c32)], hatch = "\\\\", width  = 0.1, color = "#e1e1e1")


# plt.axhline(y=1, color='r', linestyle='-')
# summ=0
# summ1=0
# for i in range(len(metal)):
#     summ=summ+metal[i]
#     # summ1=summ1
# avg=summ/len(metal)
# imp=1/avg
# print(imp)
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)


#for i in range(len(BM_name)):
 #   plt.text(i+1.1,4.0,str(nrm[i]),fontsize=font,weight="bold")


# for i in range(len(assoc4)):
#    plt.text(i+1.7,metal[i],str(nrm[i]),fontsize=16,weight="bold", ha="center")
font1=32
k=0
for i in bar1:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm128[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold")
    k=k+1
k=0
for i in bar2:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm64[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold")
    k=k+1
k=0
for i in bar3:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm32[k]), ha="center", va="bottom", fontsize=font1, color="red", weight="bold")
    k=k+1
# plt.title('Runtime Comparision', size =font)
legend = [ "256k x 1","128k x 2","64k x 4","32k x 8"]
plt.legend(legend, fontsize=34, loc='best', ncol = 4, frameon=True,handletextpad=0.1,columnspacing=0.6,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.92, 1.28))
plt.ylabel('Exe. Slowdown %', size = font, color='k')
# plt.xlabel('Benchmark', size = font, color='k')
ax.axvline(x=5.28, color='red',linewidth=4)
ax.text(5.304, 4.3, 'Eff. Capacity %', rotation=90, color='red',size=32,weight="bold")
plt.annotate("Gorgon", (0.15, -0.1), xycoords='axes fraction',
             textcoords='offset points', va='top', size=font, weight='bold')
plt.annotate("Aurochs",   (0.39,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Capstan",   (0.58,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("WidX",   (0.80,-0.1), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.ylim(-20,100)
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/shared_latency.pdf')
# plt.show()