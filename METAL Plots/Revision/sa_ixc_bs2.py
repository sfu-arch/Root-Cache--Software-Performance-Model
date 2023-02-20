import sys

import math
# from scipy.stats import gmean



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

BM_name = ["B+Tree","Hash","Analy.","B+Tree","Hash","Analy.","B+Tree","Hash","Analy."]
metal = ([60.8, 57.3, 69.8,60.8, 57.3, 69.8,60.8, 57.3, 69.8])
sbit_cache = (([57,42,61,72,57,78,71,60,79]))
ebit_cache = (([71,53,76,81,59,81,83,63,84]))
tbit_cache = (([53,37,56,69,54,70,70,57,73]))
# scaling=([1,3.17,4.32,3.62])
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


xticks_minor = [ 3.5, 6.5 ]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

summ=0
plt.bar([i - 0.2 for i in X_AXIS], [(sbit_cache[i])/(metal[i]/10) for i,X in  enumerate(sbit_cache)], hatch = "//", width  = 0.2, color = "#e9e9e9")
plt.bar([i + 0.0 for i in X_AXIS], [(ebit_cache[i])/(metal[i]/10) for i,X in  enumerate(ebit_cache)], hatch = ".", width  = 0.2, color = "gray")
plt.bar([i + 0.2 for i in X_AXIS], [(tbit_cache[i])/(metal[i]/10) for i,X in  enumerate(tbit_cache)], width  = 0.2, color = "#b1b1b1")
# plt.bar([i + 0.4 for i in X_AXIS], [(X/stream[i])*scaling[0] for i,X in  enumerate(stream)], hatch = "//", width  = 0.2, color = "black")
# for i in range(len(cache)):
#     summ = summ + (stream[i]/metal[i])
# print()
# print()
# avg=(summ*scaling[2])/(10*scaling[0])
# print("avg is",avg)

#geometric mean

# prod=1
# met=([0, 0, 0 , 0, 0,0,0, 0,0,0])
# for i,X in  enumerate(stream):
#     met[i] = (X/metal[i])*scaling[2] 
#     prod=prod*met[i]
# geomean=math.pow(prod,len(stream))
# print("trial",geomean)

# #calculate geometric mean
# geom=gmean(met)

# # plt.plot(0, y, '-r', label='y=2x+1')
# with open('hbm_Values', 'w') as f:
#     # f.writelines(lines)

#     f.write("metal:\n")

#     for i in range(len(metal)):
#         f.write(str((stream[i]/metal[i])*scaling[2]))
#         f.write("\n")
#     f.write("cache:\n")
#     for i in range(len(cache)):
#         f.write(str((stream[i]/cache[i])*scaling[1]))
#         f.write("\n")
#     f.write("stream:\n")
#     for i in range(len(stream)):
#         f.write(str((stream[i]/stream[i])*scaling[0]))
#         f.write("\n")
# f.close()
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["6b Block Size","8b Block Size", "10b Block Size"]
plt.legend(legend, fontsize=font, loc='best', ncol = 4, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.75, 1.15))
# plt.axhline(geom, color = 'r', linestyle = 'dotted',linewidth=2)

plt.ylabel('Norm. Performance', size = font, color='k')
# plt.ylim([0,25])
# plt.xlabel('Benchmark', size = font, color='k')

plt.annotate("4-way",     (0.16,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
plt.annotate("8-way",   (0.47,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("16-way",   (0.78,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/sa_ixc_bs2.pdf')
plt.show()