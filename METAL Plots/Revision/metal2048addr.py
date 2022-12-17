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

font = 18

BM_name = ['8kB', '16kB ', '32kB' , "64kB",'8kB', '16kB ', '32kB' , "64kB",'8kB', '16kB ', '32kB' , "64kB",'8kB', '16kB ', '32kB' , "64kB",'8kB', '16kB ', '32kB' , "64kB"]
stream =     ([0.26,0.56,1.04,1.43,0.21,0.43,0.98,1.28,0.18,0.39,0.81,1.17,0.29,0.58,1.06,1.37,0.37,0.72,1.18,1.4])
# cache = ([101, 113, 126, 33,56,900,960, 4831,102,5721])
# metal = (([48, 57, 42, 18,20,480,507, 2889,41,2906]))
# scaling =([1, 1.15, 1.06])

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


xticks_minor = [ 4.5,  8.5, 12.5, 16.5]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

bar1= plt.bar([i + 0.25 for i in X_AXIS], [(stream[i])for i,X in  enumerate(stream)], hatch = "--", width  = 0.55, color = "black")
# plt.bar([i + 0.05 for i in X_AXIS], [(cache[i] )for i,X in  enumerate(stream)], width  = 0.2, color = "#b1b1b1")
# plt.bar([i - 0.14 for i in X_AXIS], [(metal[i]) for i,X in  enumerate(stream)], width  = 0.2,  hatch = "//", color = "#e9e9e9")

# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)ß
# legend = ["Stream"]
# plt.legend(legend, fontsize=font, loc='best', ncol = 1, frameon=True,
#            facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 0.7))

plt.ylabel('Norm. Effectiveness', size = font, color='k')
plt.ylim([0, 1.5])
height = bar1[19].get_height()
plt.text(bar1[19].get_x() + bar1[19].get_width()/2.0, height, "4x", ha="center", va="bottom", fontsize=font, color="red", weight="bold")

plt.annotate("B+Tree",     (0.07,-0.22), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
plt.annotate("Hash",     (0.25,-0.22), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
plt.annotate("RTree",     (0.47,-0.22), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Analytics",   (0.62,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("SpMM",     (0.82,-0.22), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/metal2048addr.pdf')
plt.show()