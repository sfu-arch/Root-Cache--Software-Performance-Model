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




stream =[]
metal=[]
cache =[]

font = 32

BM_name = ['B+Tree' , "Hash", "SpMV","Analytics","SpMM"]
cache = ([30*9000/15000, 25*9000/15000,42*9000/15000,16*9000/15000,40*9000/15000])
assoc4 = ([30*8000/15000, 25*8000/15000,42*8000/15000, 16*8000/15000,40*8000/15000])

metal = ([1,1,1,1,1])
for i in range(len((cache))):
    cache[i]=cache[i]/8
    assoc4[i]=assoc4[i]/8

for i in range(len(cache)):
    metal[i]=metal[i]/cache[i]
    assoc4[i]=assoc4[i]/cache[i]
    cache[i]=cache[i]/cache[i]
    
nrm = [3.8, 3.1, 5.3, 2, 5]

X_AXIS = np.linspace(3,len(BM_name),len(BM_name))



fig,ax=plt.subplots(figsize=(18, 10))
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


xticks_minor = [ 3.5,4.5, 5.5, 8.5, 12.5 ]

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

# plt.bar([i - 0.20 for i in X_AXIS], [stream[i]/X for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")
bar1 = plt.bar([i - 0.15 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], hatch = "//", width  = 0.2, color = "#e7e7e7")
plt.bar([i + 0.05 for i in X_AXIS], [assoc4[i] for i,X in  enumerate(cache)], hatch = "", width  = 0.2, color = "black")
plt.axhline(y=1, color='r', linestyle='-')
summ=0
for i in range(len(metal)):
    summ=summ+metal[i]
avg=summ/len(metal)
imp=1/avg
print(imp)
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)


#for i in range(len(BM_name)):
 #   plt.text(i+1.1,4.0,str(nrm[i]),fontsize=font,weight="bold")


# for i in range(len(assoc4)):
#    plt.text(i+1.7,metal[i],str(nrm[i]),fontsize=16,weight="bold", ha="center")

k=0
for i in bar1:
    height = i.get_height()
    plt.text(i.get_x() + i.get_width()/2.0, height, str(nrm[k]) + 'x', ha="center", va="bottom", fontsize=font, color="red", weight="bold")
    k=k+1
# plt.title('Runtime Comparision', size =font)
legend = ["FA-Addr","METAL","Ideal 4-way"]
plt.legend(legend, fontsize=36, loc='best', ncol = 3, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1, 1.125))
plt.ylabel('Norm. Cache Energy ', size = font, color='k')
plt.xlabel('Benchmark', size = font, color='k')


# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')

# Uncomment to savefig
plt.savefig('./Plots/pdfs/Onchip_Energy.pdf')
plt.show()