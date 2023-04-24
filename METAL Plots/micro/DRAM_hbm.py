import sys

import math
from scipy.stats import gmean
# import scipy

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




stream =[]
metal=[]
cache =[]

font = 18

BM_name = ['SCAN 40%' , "WHERE", "JOIN","Nest.Scan","RTree","PageRank","SpMM","SpMV","KVStore","G.Mean"]
stream = ([167,1136,6368,1089,8371,68,182,138,48,1])
cache = ([101,960,4831,900,5721,57,102,67,33,0])
metal = (([42,507,2889,480,2906,30,41,20,18,0]))
metalix = (([42,507,2889/1.1,480,2906,30,41,20,18,0]))
xcache = (([94,802,4026,756,5006,49,78,31,31,0]))
scaling =([1, 1.15, 1.18,1.14])

X_AXIS = np.linspace(1,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(18, 3))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 0)
plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')


xticks_minor = [ 3.5,6.5, 8.5,9.5,10.5]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =4 )
plt.yticks(fontsize = font, color='k')
prod=1
met=([ 0 , 0, 0,0,0, 0,0,0,0])
metix=([ 0 , 0, 0,0,0, 0,0,0,0])
xc=([ 0 , 0, 0,0,0, 0,0,0,0])
c=([ 0 , 0, 0,0,0, 0,0,0,0])
for i,X in  enumerate(stream):
    if(i==9):
        break
    met[i]=(metal[i]/X)*scaling[2]
    metix[i]=(metalix[i]/X)*scaling[2]
    xc[i]=(xcache[i]/X)*scaling[3]
    c[i]=(cache[i]/X)*scaling[1]
    # prod=prod*met[i]

metal[-1]=gmean(met)*stream[-1]/scaling[2]
metalix[-1]=gmean(metix)*stream[-1]/scaling[2]
cache[-1]=gmean(c)*stream[-1]/scaling[1]
xcache[-1]=gmean(xc)*stream[-1]/scaling[3]
print("geomeans metal, xcache, cache")

print(metal[-1])
print(xcache[-1])
print(cache[-1])

ax.set_xticklabels(BM_name)

plt.bar([i - 0.15 for i in X_AXIS], [(metal[i]/X)*scaling[2] for i,X in  enumerate(stream)], width  = 0.15,  hatch = "//", color = "#e9e9e9")
plt.bar([i - 0.0 for i in X_AXIS], [(metalix[i]*1.37/X)*scaling[2] for i,X in  enumerate(stream)], width  = 0.15,  color = "#e5e5e5")
plt.bar([i + 0.15 for i in X_AXIS], [(xcache[i]/X )*scaling[3]for i,X in  enumerate(stream)], width  = 0.15,hatch=".", color = "gray")
plt.bar([i + 0.30 for i in X_AXIS], [(cache[i]/X )*scaling[1]for i,X in  enumerate(stream)], width  = 0.15, color = "#b1b1b1")
plt.bar([i + 0.45 for i in X_AXIS], [(stream[i]/X)*scaling[0] for i,X in  enumerate(stream)], hatch = "--", width  = 0.15, color = "black")

summ=0
# for i in range(len(cache)):
#     summ = summ + (xcache[i]/metal[i])
# print()
# print()
# avg=(summ*scaling[2])/(10*scaling[3])
# summ = summ + (xcache[5]/metal[5])
# avg=(summ*scaling[2])/(scaling[1])
# print("avg is",avg)




# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)ß
legend = ["METAL","METAL-IX","X-Cache" ,"Addr", "Stream"]
# plt.legend(legend, fontsize=font, loc='best', ncol = 5, frameon=True,
#            facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 1.2))
# plt.axhline(geom, color = 'r', linestyle = 'dotted',linewidth=2)
plt.ylabel('DRAM Energy', size = font, color='k',loc="center")
plt.ylim([0, 1.1])
# plt.xlabel('\n\n DSAs', size = font, color='k')

plt.annotate("Gorgon",     (0.11,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

plt.annotate("Aurochs",(0.4,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
plt.annotate("Capstan",   (0.65,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("WidX",   (0.79,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()


print("geomeans:")

metal[-1]=(metal[-1]/stream[-1])*scaling[2]
metalix[-1]=(metalix[-1]*1.37/1)*scaling[2] 
xcache[-1]=(xcache[-1]/1)*scaling[3]
cache[-1]=(cache[-1]/1 )*scaling[1]
stream[-1]=(stream[-1]/1)*scaling[0]


print("Metal","metalix","xcache","cache","stream")
print(metal[-1],metalix[-1],xcache[-1],cache[-1],stream[-1])

# Uncomment to savefig
plt.savefig('./Plots/pdfs/DRAM_HBM.pdf')
# plt.show()