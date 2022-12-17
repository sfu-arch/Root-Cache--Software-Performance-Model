# import os
# import matplotlib.pyplot as plt
# import seaborn as sns
# import cv2
# import numpy as np
# def read_file(path):
#     f = open(path)
#     lines = f.readlines()
#     start = 2
#     end = start + 10
#     all = []
#     for idx in range(10):
#         n = []
#         for l in lines[start:end]:
#             print(l.strip())
#             n.append(int(l.strip()))
#         all.append(n)
#         start+=13
#         end+=13    


#     return all

# numbers = read_file('ran_stack.txt')
# fig, ax = plt.subplots()
# #define data
# labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10']
# numbers= np.array(numbers)
# Level_0 = np.array(numbers[:,0])
# Level_1 = np.array(numbers[:,1])
# Level_2 = np.array(numbers[:,2])
# Level_3 = np.array(numbers[:,3])
# Level_4 = np.array(numbers[:,4])
# Level_5 = np.array(numbers[:,5])
# Level_6 = np.array(numbers[:,6])
# Level_7 = np.array(numbers[:,7])
# Level_8 = np.array(numbers[:,8])
# Level_9 = np.array(numbers[:,9])



# width = 0.35 
# ax.bar(labels, Level_0, width, label='Level_0')
# ax.bar(labels, Level_1, width,
#        label='Level_1', bottom=Level_0)
# ax.bar(labels, Level_2, width,
#        label='Level_2', bottom=Level_1 + Level_0)
# ax.bar(labels, Level_3, width,
#        label='Level_3', bottom=Level_1 + Level_0 + Level_2)
# ax.bar(labels, Level_4, width,
#        label='Level_4', bottom=Level_1 + Level_0 + Level_2 + Level_3)
# ax.bar(labels, Level_5, width,
#        label='Level_5', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4)
# ax.bar(labels, Level_6, width,
#        label='Level_6', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5)
# ax.bar(labels, Level_7, width,
#        label='Level_7', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6)
# ax.bar(labels, Level_8, width,
#        label='Level_8', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6 + Level_7)
# ax.bar(labels, Level_9, width,
#        label='Level_9', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6 + Level_7 + Level_8)

# ax.set_ylabel('Cache Occupancy')
# ax.set_xlabel('Time Step')
# ax.set_title('Random Root Cache Snapshot')
# ax.legend()
# plt.savefig('testr.png')



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

factor=[]
factor=[0.986, 0.992, 0.998, 0.97, 0.9987, 0.9941]
k=0
def read_file(path):
    k=0
    f = open(path)
    lines = f.readlines()
    start = 2
    end = start + 5
    all=[]
    for idx in range(6):
        n = []
        for l in lines[start:end]:
            print(l.strip())
            n.append((float(l.strip())*factor[k]))
        n.insert(0,(1-(n[0]+n[1]+n[2]+n[3]+n[4])))
        
        all.append(n)
        k=k+1
        start+=8
        end+=8    


    return all

# from palettable.colorbrewer.sequential import YlGnBu_5

percentage = read_file("benchstack.txt")
# onemin = []
# for i in range(length(all)):
#     for j in range(length(all[i])):
#         onemin[k]=onemin[k]+all
mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

# import matplotlib.patches as mpatches
# import matplotlib.pyplot as plt
# legend=['7-9','6','5','4','1-3']    
font = 24
# a_val=0.6
# colors = ['#cce6ff','#ffeca9','#d099e2','#ccd1f1','#86ac3f',"black"]
# circ1 = mpatches.Patch( facecolor=colors[0],alpha=a_val,hatch='',label='Level 7-9')
# circ2= mpatches.Patch( facecolor=colors[1],alpha=a_val,hatch='///',label='Level 6')
# circ3 = mpatches.Patch(facecolor=colors[2],alpha=a_val,hatch='',label='Level 5')
# circ4= mpatches.Patch( facecolor=colors[3],alpha=a_val,hatch='///',label='Level 4')
# circ5 = mpatches.Patch(facecolor=colors[4],alpha=a_val,hatch='',label='Level 1-3')
# circ6 = mpatches.Patch(facecolor=colors[5],alpha=a_val,hatch='',label='MISS')

# plt.legend(handles=[circ1,circ2,circ3,circ4,circ5,circ6], ncol=3, fontsize=font, loc='upper center', fancybox=False, handletextpad=0.1, labelspacing=0, bbox_to_anchor=(0.7,1.18))




BM = [ "Rand. 100%","Rand. 80%" ,"Rand. 40%", "Hash", "SpMV","SpMM"]
# percentage = [[87, 8, 5], [87, 8, 5], [87, 2, 10], [92, 7, 1],  [87, 2, 10] ]legend = ["Level 1", "Level 2", "Level 3", "Level 4","Level 5", "Level 6", "Level 7", "Level 8", "Level 9","Level 10"]
#plt.legend(legend, fontsize=font, loc='upper center', ncol = 2, frameon=True,
          # facecolor='w', edgecolor='k', fancybox=False, handletextpad=0.1, labelspacing=0, bbox_to_anchor=(0.5,1.3))
# percentage = [[75, 25],[75, 25],[65,34], [96 , 4], [65,34] ]
# percentage = [[66, 6, 4, 24 ], [66, 6, 4, 24 ], [ 66, 1.5, 6.5, 26 ], [89, 6.5 , 0.9, 3.6], [ 66, 1.5, 6.5, 26 ]]

fig,ax=plt.subplots(figsize=(15, 8))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
ax.tick_params(axis='y', which='minor', left=False)

xticks_minor = [ 2.5 ]
ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(rotation=20 , rotation_mode = 'anchor', va="top", fontsize = font ,ha= 'right', color='k')
plt.yticks(fontsize = font, color='k')


# X_AXIS = np.linspace(1.5,len(BM_name),len(BM_name))
width = 0.7

for (i, bm) in enumerate(BM):
    dataset = percentage[i]
    p1 = plt.bar(bm, dataset[0], width, color='black')
    p2 = plt.bar(bm, dataset[1], width, bottom=dataset[0], color='#cce6ff', hatch='')
    p3 = plt.bar(bm, dataset[2], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]),  color='#ffeca9',  hatch='')
    p4 = plt.bar(bm, dataset[3], width, 
                bottom=(np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])), color='#d099e2',  hatch='//'  )
    p5 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3]), color='#ccd1f1',  hatch=''  )
    p6 = plt.bar(bm, dataset[5], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4]), color='#86ac3f',  hatch=''  )
    
    '''
    
     
    p7 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[4]), color='#86ac3f',  hatch=''  )
    p8 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4]), color='#86ac3f',  hatch=''  )
    p9 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4]), color='#86ac3f',  hatch=''  )
    p10 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4])+np.array(dataset[4]), color='#86ac3f', hatch='' )
    

'''

# plt.title('Runtime Normalized To Hit_rate = 0', size =font)


plt.annotate("B+ Tree Search",     (0.12,-0.12), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')


plt.ylabel('Norm. Levels Traversed per Hit', size = font, color='k')
# plt.xlabel('Time Step', size = font, color='k')
# plt.xlabel('DSAs', size = font, color='k')
    
plt.tight_layout()
plt.savefig('./Plots/pdfs/levelstraversedperhit.pdf')

# plt.savefig('./Plots/pdfs/legend.pdf')
plt.show()