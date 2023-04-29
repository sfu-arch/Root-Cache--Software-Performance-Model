# import sys

# import math


# import matplotlib.pyplot as plt
# import matplotlib as mpl
# import matplotlib
# import numpy as np
# from matplotlib.backends.backend_pdf import PdfPages
# from matplotlib.ticker import MultipleLocator
# from random import randint
# from matplotlib.backends.backend_pdf import PdfPages
# from matplotlib.backends.backend_pdf import PdfPages
# import matplotlib.ticker as ticker
# import csv

# print(sys.path)

# # from palettable.colorbrewer.sequential import YlGnBu_5

# mpl.rc('font', family='sans-serif')
# matplotlib.style.use('ggplot')

# font = 24
# X_AXIS_name = []
# X_AXIS = np.linspace(0.1, 0.9, 9)




# stream =[]
# metal=[]
# cache =[]

# font = 18

# BM_name = ['Random', 'Sk80', 'Sk40' , "Hash Table", "SpMV","SELECT","WHERE","JOIN","SpMM"]
# cache = ([21*890/583, 24*890/583, 30*890/583, 25*890/583,42*890/583,21*890/583,18*890/583, 16*890/583,40*890/583])
# metal = ([1,1,1,1,1,1,1,1,1])
# for i in range(len((cache))):
#     cache[i]=cache[i]/8

# X_AXIS = np.linspace(1,len(BM_name),len(BM_name))


# fig,ax=plt.subplots(figsize=(18, 5))
# ax.set_facecolor('w')
# ax.set_axisbelow(True)
# ax.spines['bottom'].set_color('k')
# plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
# plt.gca().xaxis.grid(False)
# plt.gca().yaxis.grid(True)

# ax.tick_params(axis='y', which='minor', left=False)
# plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
# plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 20)
# plt.xticks(size=font, va="top")
# plt.yticks(fontsize = font, color='k')


# xticks_minor = [ 3.5,4.5, 5.5, 8.5, 12.5 ]

# ax.set_xticks( xticks_minor, minor=True )

# ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
# plt.yticks(fontsize = font, color='k')

# ax.set_xticklabels(BM_name)

# # plt.bar([i - 0.20 for i in X_AXIS], [stream[i]/X for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")
# plt.bar([i + 0.05 for i in X_AXIS], [cache[i] for i,X in  enumerate(cache)], hatch = "||", width  = 0.2, color = "black")
# plt.bar([i - 0.15 for i in X_AXIS], [metal[i] for i,X in  enumerate(metal)], hatch = "//", width  = 0.2, color = "#D5D5D5")

# # plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# # plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# # plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# # plt.title('Runtime Comparision', size =font)
# legend = ["Address based cache","Metal"]
# plt.legend(legend, fontsize=font, loc='best', ncol = 1, frameon=True,
#            facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 1.0))
# plt.ylabel('Norm. Cache Access ', size = font, color='k')
# # plt.xlabel('\n\n DSAs', size = font, color='k')

# plt.annotate("B+ Tree Search",     (0.09,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# # plt.annotate("Hash\nTable",(0.37,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# # plt.annotate("SpMV",   (0.47,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# # plt.annotate("SpMM",   (0.9,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("Data Analytics",   (0.62,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.tight_layout()
# # Uncomment to savefig
# plt.savefig('./RuntimeCompare3.pdf')
# plt.show()

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

font = 48
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)




stream =[]
metal=[]
cache =[]


font = 48

BM_name = ["Scan" , "JOIN", "SpMV","KVStore","Solver", "RTree"]
# gather = ([2.2, 0, 0, 1.71, 0.624,0])
# no_pattern = ([1,1,1,1,1,1])
# fetch  = ([0, 1.82, 3.8, 0, 0,0])
# filter = ([0, 0, 0, 0, 2.4,0])
# gatfilter = ([0,0,0,0,0,3.17])
# gather = ([	2.2,	1.71,	0,	0.624,	0,	0	])
# no_pattern = (	[1,	1,	1	,1,	1,	1]	)
# fetch = (	[0,	0,	0	,0,	3.8	,1.82]	)
# filter = (	[0	,0,	0,	2.4	,0,	0	])
# gatfilter = (	[0,	0,	3.17,	0,	0,	0]	)

gather = ([	2.2,	1.71,	0	,0	,0.624,	0]	)
no_pattern = (	[1,1,	1	,1,	1	,1]	)
fetch = (	[0,	0	,3.8,	1.82,	0,	0]	)
filter = (	[0,	0	,0,	0,	2.4,	0]	)
gatfilter = (	[0,	0,	0	,0,	0,	3.17]	)


X_AXIS = np.linspace(2.5,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(22, 10))
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

for i in range(len(gatfilter)):
    if(gather[i]>0):
        gather[i]=1/gather[i]
    if(filter[i]>0):
        filter[i]=1/filter[i]
    if(fetch[i]>0):
        fetch[i]=1/fetch[i]
    if(gatfilter[i]>0):
        gatfilter[i]=1/gatfilter[i]
xticks_minor = [ 3.5,4.2, 5, 9.5, 12.5 ]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)

# plt.bar([i - 0.20 for i in X_AXIS], [stream[i]/X for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")
plt.bar([i + 0.05 for i in X_AXIS], [no_pattern[i] for i,X in  enumerate(no_pattern)], hatch = "||", width  = 0.2, color = "black")
plt.bar([i - 0.15 for i in X_AXIS], [gather[i] for i,X in  enumerate(gather)], hatch = "//", width  = 0.2, color = "#C5C5C5")
plt.bar([i - 0.15 for i in X_AXIS], [fetch[i] for i,X in  enumerate(fetch)], width  = 0.2, color = "#D5D5D5")
plt.bar([i + 0.25 for i in X_AXIS], [filter[i] for i,X in  enumerate(filter)], width  = 0.2, color = "#A5A5A5")
plt.bar([i + 0.25 for i in X_AXIS], [gatfilter[i] for i,X in  enumerate(gatfilter)], width  = 0.2, color = "#b1b1b1", hatch=".")
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["METAL-IX","Gather", "Fetch", "Filter","Gather + Filter"]
plt.legend(legend, fontsize=33, loc='best', ncol = 5, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1.01, 1.15))
plt.ylabel('Norm. Walk Latency ', size = font, color='k')
# plt.xlabel('\n\n DSAs', size = font, color='k')
font1=44
plt.annotate("Gorgon",     (0.09,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font1 ,weight='bold')

plt.annotate("Capstan",(0.34,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font1 ,weight='bold')
plt.annotate("WidX",   (0.54,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font1,weight='bold')
plt.annotate("Aurochs",   (0.74,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = font1,weight='bold')
# plt.annotate("Data Analytics",   (0.62,-0.15), xycoords='axes fraction', textcoords='offset points', va='top', size = 40,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/PatternCompare.pdf')
# plt.show()