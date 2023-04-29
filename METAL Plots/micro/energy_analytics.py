# import matplotlib.pyplot as plt
# import numpy as np

# font=16
# btree = np.array([30560,
# 54330,
# 28970])

# analy=np.array([232190,
# 142350,
# 35090])
# # labels=['Compute','IX-Cache','Pattern Controller']
# colour=['#fdb73e','#7a77e6','#4adede']
# plt.pie(analy, autopct='%1.1f%%',colors=colour,textprops={'fontsize': font})
# plt.savefig('Plots/pdfs/energy_analytics.pdf')

import sys

import math


import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
import numpy as np
from statistics import mean
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

font = 50
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
BM_name = ("Scan",	"JOIN",	"RTree"	,"SpMM","KVStore")
# walk= [84, 91, 62 , 51, 37, 79, 48, 53]
# compute= [16,9,38,49,63,21,52,47]
# walk=	np.array([37,	79	,48	,53,	62,	51	,91])
# compute=	np.array([33	,20,	32,	17,	19	,9,	4])
# add=	np.array([30	,1,	20,	30,	19	,40,	5])
compute=	np.array([36.35,	61.87	,49.42	,49.96,	34.31])
ixc=	np.array([47.29	,26.89,	17.83,	28.12,	27.14])
pc=	np.array([16.35	,11.25,32.75,	21.92,	38.55])
# X_AXIS = np.linspace(0,len(BM_name),len(BM_name))

print("comp,ixc,walk")
print(mean(compute),mean(ixc),mean(pc))


fig,ax=plt.subplots(figsize=(26, 10))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['left'].set_color('k')
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(True)
plt.gca().yaxis.grid(False)
# xticks_minor = [ 1.5,3.5,5.4]

# # ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')
plt.xticks(fontsize = font, color='k')
ax.set_yticklabels(BM_name)


ax.tick_params(axis='y', which='minor', left=False)
# # plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
# # plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 0)
# plt.xticks(size=font, va="top",color="k")
# plt.yticks(fontsize = font, color='k')
ax.set_xlabel('% Energy Breakdown', fontsize=font,color='k')

# # Set the y-axis ticks and labels
# ax.set_yticks(range(len(BM_name)))
# ax.set_yticklabels(BM_name, fontsize=14)

# Add a legend
legend = ["Walk", "Compute", "Add"]
ax.legend(legend, loc='lower right')

# plt.barh(BM_name, walk, color='black')
# plt.barh(BM_name, compute, left=walk, color='grey')
# plt.barh(BM_name, add, left=compute+walk, color='green')
bar_height = 0.25
bar_y = np.arange(len(BM_name))
# ax.barh(bar_y - bar_height, walk, height=bar_height, label="Walk", color='black')
# ax.barh(bar_y, compute, height=bar_height, label="Compute", color='grey')
# ax.barh(bar_y + bar_height, add, height=bar_height, label="Add", color='green')
ax.barh(BM_name, compute, color='black',height=0.6)
ax.barh(BM_name, ixc, left=compute, color='#d8d8d8',height=0.6)
ax.barh(BM_name, pc, left=compute+ixc, color='grey',height=0.6)

# plt.xlabel('% Execution Time', fontsize=48, color='k')
# plt.annotate("Gorgon",     (0.12,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40 ,weight='bold')

# plt.annotate("Aurochs",(0.42,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40 ,weight='bold')
# plt.annotate("Capstan",   (0.65,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40,weight='bold')
# plt.annotate("WidX",   (0.88,-0.13), xycoords='axes fraction', textcoords='offset points', va='top', size = 40,weight='bold')
# plot bars in stack manner
plt.xlim(0,100)


legend = ["Compute","IX-cache", "Walker", "Filter","Gather + Filter"]
plt.legend(legend, fontsize=48, loc='best', ncol = 3, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.91, 1.26))
plt.tight_layout()
plt.savefig('./Plots/pdfs/energy_analytics.pdf')
# plt.show()
