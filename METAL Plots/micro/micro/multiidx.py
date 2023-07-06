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
# import matplotlib.patches as mpatches

# print(sys.path)


# # all = []
# font=24
# def read_file(path):
#     f = open(path)
#     lines = f.readlines()
#     start = 2
#     end = start + 5
#     all=[]
#     for idx in range(12):
#         n = []
#         for l in lines[start:end]:
#       #      print(l.strip())
#             n.append(float(l.strip()))
#         all.append(n)
#         start+=8
#         end+=8   


#     return all

# # from palettable.colorbrewer.sequential import YlGnBu_5

# percentage = read_file("idxmultilevcache.txt")
# #print("\n\npercentage\n\n",percentage)

# mpl.rc('font', family='sans-serif')
# matplotlib.style.use('ggplot')
# legend=['1-3','4','5','6','7-10']    

# a_val=0.6
# colors = ['#cce6ff','#ffeca9','#d099e2','#ccd1f1','#86ac3f']
# circ1 = mpatches.Patch( facecolor=colors[0],alpha=a_val,hatch='',label='Level 1-3')
# circ2= mpatches.Patch( facecolor=colors[1],alpha=a_val,hatch='',label='Level 4')
# circ3 = mpatches.Patch(facecolor=colors[2],alpha=a_val,hatch='',label='Level 5')
# circ4= mpatches.Patch( facecolor=colors[3],alpha=a_val,hatch='///',label='Level 6')
# circ5 = mpatches.Patch(facecolor=colors[4],alpha=a_val,hatch='',label='Level 7-10')

# font = 24




# #BM = [ ".", "OPT", ".", "OPT", "."," OPT",".","OPT",".","OPT",".","OPT"]

# BM = [ "FX", "++", " FX", " ++", "  FX","   ++","   FX","  ++","    FX","    ++","      FX","        ++"]
# # percentage = [[87, 8, 5], [87, 8, 5], [87, 2, 10], [92, 7, 1],  [87, 2, 10] ]legend = ["Level 1", "Level 2", "Level 3", "Level 4","Level 5", "Level 6", "Level 7", "Level 8", "Level 9","Level 10"]

# # percentage = [[75, 25],[75, 25],[65,34], [96 , 4], [65,34] ]
# # percentage = [[66, 6, 4, 24 ], [66, 6, 4, 24 ], [ 66, 1.5, 6.5, 26 ], [89, 6.5 , 0.9, 3.6], [ 66, 1.5, 6.5, 26 ]]

# fig,ax=plt.subplots(figsize=(12, 6.55))
# ax.set_facecolor('w')
# ax.set_axisbelow(True)
# ax.spines['bottom'].set_color('k')
# plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
# plt.gca().xaxis.grid(False)
# plt.gca().yaxis.grid(True)
# ax.tick_params(axis='y', which='minor', left=False)
# plt.tick_params(axis='both', which='major', direction='in', length=6, width=5)

# plt.xticks(rotation=90, va ="top", fontsize = 24 ,ha= 'center', color='k',position=(0,0))
# plt.yticks(fontsize = 24, color='k')

# # xticks_minor = [3.5,6.5,8.5, 9.5,10.5 ]

# # ax.set_xticks( xticks_minor, minor=True )

# width = 0.6

# for (i, bm) in enumerate(BM):
#     dataset = percentage[i]
#     p1 = plt.bar(bm, dataset[0], width, color='#cce6ff')
#     p2 = plt.bar(bm, dataset[1], width, bottom=dataset[0], color='#ffeca9', hatch='')
#     p3 = plt.bar(bm, dataset[2], width, 
#                 bottom=np.array(dataset[1])+np.array(dataset[0]),  color='#d099e2',  hatch='')
#     p4 = plt.bar(bm, dataset[3], width, 
#                 bottom=(np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])), color='#ccd1f1',  hatch='//'  )
#     p5 = plt.bar(bm, dataset[4], width, 
#                 bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3]), color='#86ac3f',  hatch=''  )

# xticks_minor = [ 1.3,3.3,5.3,7.3,9.3]
# ax.set_xticks( xticks_minor, minor=True )

# ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
# plt.annotate("Scan",(0.0,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
# plt.annotate("JOIN",(0.20,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
# plt.annotate("RTree",(0.35,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font)
# plt.annotate("SpMM",(0.51,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
# plt.annotate("SpMV",(0.66,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
# plt.annotate("KVStore",(0.83,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )

# plt.legend([circ1,circ2,circ3,circ4,circ5], legend, fontsize=24, loc='upper center', ncol = 5, frameon=True,
#           facecolor='w', edgecolor='k', fancybox=False, handletextpad=0.15, labelspacing=0, bbox_to_anchor=(0.5,1.2))
# plt.annotate("Gorgon",     (0.12,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Aurochs",(0.34,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("Capstan",   (0.56,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("WidX",   (0.85,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')

# plt.ylabel('Cache Occupancy', size = 24, color='k')
# # plt.xlabel('Benchmarks', size = font, color='k')
# # plt.xlabel('DSAs', size = font, color='k')
    
# plt.tight_layout()
# plt.savefig('./Plots/pdfs/multiidx2.pdf')
# # plt.show()

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
import matplotlib.patches as mpatches

print(sys.path)


# all = []
font=24
def read_file(path):
    f = open(path)
    lines = f.readlines()
    start = 2
    end = start + 5
    all=[]
    for idx in range(12):
        n = []
        for l in lines[start:end]:
      #      print(l.strip())
            n.append(float(l.strip()))
        all.append(n)
        start+=8
        end+=8   


    return all

# from palettable.colorbrewer.sequential import YlGnBu_5

percentage = read_file("idxmultilevcache.txt")
#print("\n\npercentage\n\n",percentage)

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')
legend=['1-3','4','5','6','7-10']    

a_val=0.6
colors = ['#cce6ff','#ffeca9','#d099e2','#ccd1f1','#86ac3f']
circ1 = mpatches.Patch( facecolor=colors[0],alpha=a_val,hatch='',label='Level 1-3')
circ2= mpatches.Patch( facecolor=colors[1],alpha=a_val,hatch='',label='Level 4')
circ3 = mpatches.Patch(facecolor=colors[2],alpha=a_val,hatch='',label='Level 5')
circ4= mpatches.Patch( facecolor=colors[3],alpha=a_val,hatch='///',label='Level 6')
circ5 = mpatches.Patch(facecolor=colors[4],alpha=a_val,hatch='',label='Level 7-10')

font = 24




#BM = [ ".", "OPT", ".", "OPT", "."," OPT",".","OPT",".","OPT",".","OPT"]

BM = [ "FX", "MTL", " FX", " MTL", "  FX","   MTL","   FX","  MTL","    FX","    MTL","      FX","        MTL"]
# percentage = [[87, 8, 5], [87, 8, 5], [87, 2, 10], [92, 7, 1],  [87, 2, 10] ]legend = ["Level 1", "Level 2", "Level 3", "Level 4","Level 5", "Level 6", "Level 7", "Level 8", "Level 9","Level 10"]

# percentage = [[75, 25],[75, 25],[65,34], [96 , 4], [65,34] ]
# percentage = [[66, 6, 4, 24 ], [66, 6, 4, 24 ], [ 66, 1.5, 6.5, 26 ], [89, 6.5 , 0.9, 3.6], [ 66, 1.5, 6.5, 26 ]]

fig,ax=plt.subplots(figsize=(12, 6.55))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=5)

plt.xticks(rotation=90, va ="top", fontsize = 24 ,ha= 'center', color='k',position=(0,0))
plt.yticks(fontsize = 24, color='k')

# xticks_minor = [3.5,6.5,8.5, 9.5,10.5 ]

# ax.set_xticks( xticks_minor, minor=True )

width = 0.6

for (i, bm) in enumerate(BM):
    dataset = percentage[i]
    p1 = plt.bar(bm, dataset[0], width, color='#cce6ff')
    p2 = plt.bar(bm, dataset[1], width, bottom=dataset[0], color='#ffeca9', hatch='')
    p3 = plt.bar(bm, dataset[2], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]),  color='#d099e2',  hatch='')
    p4 = plt.bar(bm, dataset[3], width, 
                bottom=(np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])), color='#ccd1f1',  hatch='//'  )
    p5 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3]), color='#86ac3f',  hatch=''  )

xticks_minor = [ 1.3,3.3,5.3,7.3,9.3]
ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.annotate("Scan",(0.0,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
plt.annotate("JOIN",(0.20,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
plt.annotate("RTree",(0.35,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font)
plt.annotate("SpMM",(0.51,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
plt.annotate("SpMM-S",(0.66,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )
plt.annotate("KVStore",(0.83,-0.20), xycoords='axes fraction', textcoords='offset points', va='top', size = font )

plt.legend([circ1,circ2,circ3,circ4,circ5], legend, fontsize=24, loc='upper center', ncol = 5, frameon=True,
          facecolor='w', edgecolor='k', fancybox=False, handletextpad=0.15, labelspacing=0, bbox_to_anchor=(0.5,1.2))
plt.annotate("Gorgon",     (0.12,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

plt.annotate("Aurochs",(0.34,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
plt.annotate("Capstan",   (0.56,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("WidX",   (0.85,-0.3), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')

plt.ylabel('Cache Occupancy', size = 24, color='k')
# plt.xlabel('Benchmarks', size = font, color='k')
# plt.xlabel('DSAs', size = font, color='k')
    
plt.tight_layout()
plt.savefig('./Plots/pdfs/multiidx2.pdf')
# plt.show()