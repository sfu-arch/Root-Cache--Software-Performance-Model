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

BM_name = ['Rand. 100%', 'Rand. 80%', 'Rand. 40%' , "Hash", "SpMV","SELECT","WHERE","JOIN","SpMM","RTree","G.Mean"]
stream =     ([167, 167, 167 , 48, 138,1089,1136, 6368,182,8371,1])
cache = ([126, 113, 101, 33,67,900,960, 4831,102,5721,0])
metal = (([57, 48, 42, 18,20,480,507, 2889,41,2906,0]))
xcache = (([101,87,94, 31,31,756,802, 4026,78,5006,0]))
scaling =([1, 1.15, 1.06,1.14])

X_AXIS = np.linspace(1,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(18, 5))
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


xticks_minor = [ 3.5,4.5, 5.5, 8.5, 12.5,13]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')
prod=1
met=([0, 0, 0 , 0, 0,0,0, 0,0,0])
xc=([0, 0, 0 , 0, 0,0,0, 0,0,0])
c=([0, 0, 0 , 0, 0,0,0, 0,0,0])
for i,X in  enumerate(stream):
    if(i==10):
        break
    met[i]=(metal[i]/X)*scaling[2]
    xc[i]=(xcache[i]/X)*scaling[3]
    c[i]=(cache[i]/X)*scaling[1]
    # prod=prod*met[i]

metal[-1]=gmean(met)*stream[-1]/scaling[2]
cache[-1]=gmean(c)*stream[-1]/scaling[1]
xcache[-1]=gmean(xc)*stream[-1]/scaling[3]
print("geomeans metal, xcache, cache")

print(metal[-1])
print(xcache[-1])
print(cache[-1])

ax.set_xticklabels(BM_name)

plt.bar([i - 0.2 for i in X_AXIS], [(metal[i]/X)*scaling[2] for i,X in  enumerate(stream)], width  = 0.2,  hatch = "//", color = "#e9e9e9")
plt.bar([i + 0.0 for i in X_AXIS], [(xcache[i]/X )*scaling[3]for i,X in  enumerate(stream)], width  = 0.2,hatch=".", color = "gray")
plt.bar([i + 0.2 for i in X_AXIS], [(cache[i]/X )*scaling[1]for i,X in  enumerate(stream)], width  = 0.2, color = "#b1b1b1")
plt.bar([i + 0.4 for i in X_AXIS], [(stream[i]/X)*scaling[0] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")

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
legend = ["METAL","X-Cache" ,"FA-Addr", "Stream"]
plt.legend(legend, fontsize=font, loc='best', ncol = 4, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 1.1))
# plt.axhline(geom, color = 'r', linestyle = 'dotted',linewidth=2)
plt.ylabel(' Norm. DRAM TRAFFIC', size = font, color='k')
plt.ylim([0, 1.1])
# plt.xlabel('\n\n DSAs', size = font, color='k')

plt.annotate("B+ Tree Search",     (0.09,-0.22), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Data Analytics",   (0.51,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/DRAM_HBM.pdf')
plt.show()