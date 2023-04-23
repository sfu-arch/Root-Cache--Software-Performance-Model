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

# # from palettable.colorbrewer.sequential import YlGnBu_5

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

font = 48
X_AXIS_name = []
# X_AXIS = np.linspace(0, 0.2, 8)
# import matplotlib.pyplot as plt
# import numpy as np

# BM_name = ("B+Tree","KV-Store","SpMM","SpMV","WHERE","JOIN","SELECT","RTree")
# weight_counts = {
#     "Walk": np.array([84, 91, 62 , 51, 37, 79, 48, 53]),
#     "Compute": np.array([16,9,38,49,63,21,52,47]),
# }
# width=0.7
# # X_AXIS = np.linspace(3,len(BM_name),len(BM_name))

# fig, ax = plt.subplots()
bottom = np.zeros( 8)

# for boolean, weight_count in weight_counts.items():
#     p = ax.bar(BM_name, weight_count, width, label=boolean, bottom=bottom)
#     bottom += weight_count

# # ax.set_title("Number of penguins with above average body mass")
# ax.legend(loc="upper right")
# plt.ylabel('Miss rate %', size=font, color='k')
# plt.ylim(0, 100.0)
# plt.savefig('./Plots/pdfs/profiling.pdf')
# # plt.show()


# importing package
# import matplotlib.pyplot as plt

# create data
BM_name = ("WHERE" ,	"JOIN",	"Nest.\nScan"	,"RTree",	"SPMM",	"SPMV",	"KVStore")
# walk= [84, 91, 62 , 51, 37, 79, 48, 53]
# compute= [16,9,38,49,63,21,52,47]
walk=	[37,	79	,48	,53,	62,	51	,91]
compute=	[63	,21,	52,	47,	38	,49,	9]
X_AXIS = np.linspace(0,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(21, 11))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
xticks_minor = [ 1.5,3.5,5.4]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)


ax.tick_params(axis='y', which='minor', left=False)
# plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
# plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 0)
plt.xticks(size=font, va="top",color="k")
plt.yticks(fontsize = font, color='k')

plt.bar(BM_name, walk, color='black')
plt.bar(BM_name, compute, bottom=walk, color='grey')

plt.ylabel('% Execution Time', fontsize=48, color='k')
plt.annotate("Gorgon",     (0.12,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40 ,weight='bold')

plt.annotate("Aurochs",(0.42,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40 ,weight='bold')
plt.annotate("Capstan",   (0.65,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40,weight='bold')
plt.annotate("WidX",   (0.88,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40,weight='bold')
# plot bars in stack manner
plt.tight_layout()

legend = ["Walk","Compute", "Fetch", "Filter","Gather + Filter"]
plt.legend(legend, fontsize=40, loc='best', ncol = 2, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.54, 0.905))
plt.savefig('./Plots/pdfs/profiling.pdf')
# plt.show()
