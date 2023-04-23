import sys

import math


from matplotlib import pyplot as plt
plt.style.use('ggplot')
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
# matplotlib.style.use('ggplot')

font = 32
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)




opt =[]
metal=[]
cache =[]

font = 16

BM_name = ["B+Tree", "Hash","JOIN", "SpMM","RTree"]
ac = [1,1,1,1,1]
xcache = [0.73,0.87,0.706,0.43,0.91]
metal = [0.2,0.5,0.3,0.167,0.44]
opt=[ 0.92, 0.89,0.86,0.87,0.94]
scaling=[0.76,0.97,0.83,0.96,0.985]

X_AXIS = np.linspace(-3,len(BM_name),len(BM_name))

for i in range(len(scaling)):
    ac[i]=ac[i]*scaling[i]*100
    xcache[i]=xcache[i]*scaling[i]*100
    metal[i]=metal[i]*scaling[i]*100
    opt[i]=opt[i]*scaling[i]*100

fig,ax=plt.subplots(figsize=(10, 4))
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


xticks_minor = [ 0]
ax.set_xticks( xticks_minor, minor=True )

# ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )



plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)



plt.bar([i -0.42 for i in X_AXIS], [metal[i]/ac[i] for i,X in  enumerate(metal)], width  = 0.4,  hatch = "//", color = "#e9e9e9")
plt.bar([i + 0.0 for i in X_AXIS], [xcache[i]/ac[i] for i,X in  enumerate(xcache)], width  = 0.4, color = "gray",hatch=".")
plt.bar([i +0.42 for i in X_AXIS], [opt[i]/ac[i] for i,X in  enumerate(opt)], hatch = "--", width  = 0.4, color = "black")
plt.bar([i +0.84 for i in X_AXIS], [ac[i]/ac[i] for i,X in  enumerate(ac)], width  = 0.4, color = "#b1b1b1")

# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["METAL","X-Cache","FA-OPT","FA-Addr" ]
plt.legend(legend, fontsize=16, loc='best', frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.951, 1.2),ncol = 4)

plt.ylabel('Norm. Working Set', size = font, color='k')
# plt.ylim(0,100.0)
print("METAL","XCache","OPT","PREF")
for i in range(len(metal)):
    print(metal[i],end=",")

print()

for i in range(len(metal)):
    print(xcache[i]/ac[i],end=",")

print()
for i in range(len(metal)):
    print(opt[i]/ac[i],end=",")
print()

for i in range(len(metal)):
    print(ac[i]/ac[i],end=",")
print()


# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/cr_ws.pdf')
plt.show()

