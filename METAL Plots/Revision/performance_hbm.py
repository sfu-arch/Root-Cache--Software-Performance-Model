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

font = 16

BM_name = ['Rand. 100%', 'Rand. 80%', 'Rand. 40%' , "Hash", "SpMV","SELECT","WHERE","JOIN","SpMM","RTree"]
stream =     ([12.62, 9.31, 8.21 , 2.36, 4.96,13.42,18.33,21.42, 10.06,22.46])
cache = ([7.28, 7.17, 7.03, 1.81, 3.03,10.79,14.08,19.76,7.83,20.62])
metal = (([5.17, 2.54, 1.83 , 1.15, 1.08,5.96,9.62,11.31,2.26,15.16]))
xcache = (([7.06, 7.04, 6.93 , 1.74, 1.17,8.37,13.78,18.27,4.78,19.96]))
scaling=([1,3.17,4.32,3.62])

X_AXIS = np.linspace(1,len(BM_name),len(BM_name))


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


xticks_minor = [ 3.5,4.5, 5.5, 8.5, 12.5 ]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

summ=0
plt.bar([i - 0.2 for i in X_AXIS], [(X/metal[i])*scaling[2] for i,X in  enumerate(stream)], hatch = "//", width  = 0.2, color = "#e9e9e9")
plt.bar([i + 0.0 for i in X_AXIS], [(X/xcache[i])*scaling[3] for i,X in  enumerate(stream)], hatch = ".", width  = 0.2, color = "gray")
plt.bar([i + 0.2 for i in X_AXIS], [(X/cache[i])*scaling[1] for i,X in  enumerate(stream)], width  = 0.2, color = "#b1b1b1")
plt.bar([i + 0.4 for i in X_AXIS], [(X/stream[i])*scaling[0] for i,X in  enumerate(stream)], hatch = "//", width  = 0.2, color = "black")
for i in range(len(cache)):
    summ = summ + (stream[i]/metal[i])
print()
print()
avg=(summ*scaling[2])/(10*scaling[0])
print("avg is",avg)

# plt.plot(0, y, '-r', label='y=2x+1')
with open('hbm_Values', 'w') as f:
    # f.writelines(lines)

    f.write("metal:\n")

    for i in range(len(metal)):
        f.write(str((stream[i]/metal[i])*scaling[2]))
        f.write("\n")
    f.write("cache:\n")
    for i in range(len(cache)):
        f.write(str((stream[i]/cache[i])*scaling[1]))
        f.write("\n")
    f.write("stream:\n")
    for i in range(len(stream)):
        f.write(str((stream[i]/stream[i])*scaling[0]))
        f.write("\n")
f.close()
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["METAL","X-Cache", "FA-Addr", "Stream"]
plt.legend(legend, fontsize=font, loc='best', ncol = 4, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.75, 1.15))
plt.axhline(avg, color = 'r', linestyle = '-',linewidth=2)

plt.ylabel('Norm. Speedup', size = font, color='k')
# plt.ylim([0,25])
# plt.xlabel('Benchmark', size = font, color='k')

plt.annotate("B+ Tree Search",     (0.09,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Data Analytics",   (0.62,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/Performance_HBM.pdf')
plt.show()