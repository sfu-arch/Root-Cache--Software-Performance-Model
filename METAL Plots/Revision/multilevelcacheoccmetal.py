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

def read_file(path):
    f = open(path)
    lines = f.readlines()
    start = 2
    end = start + 10
    all=[]
    for idx in range(10):
        n = []
        for l in lines[start:end]:
            print(l.strip())
            n.append(float(l.strip()))
        all.append(n)
        start+=13
        end+=13    


    return all

# from palettable.colorbrewer.sequential import YlGnBu_5

percentage = read_file("ran80_stack.txt")

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')
legend=['1-3','4','5','6','7-10']    

a_val=0.6
colors = ['#cce6ff','#ffeca9','#d099e2','#ccd1f1','#86ac3f']
circ1 = mpatches.Patch( facecolor=colors[0],alpha=a_val,hatch='',label='Level 1-3')
circ2= mpatches.Patch( facecolor=colors[1],alpha=a_val,hatch='///',label='Level 4')
circ3 = mpatches.Patch(facecolor=colors[2],alpha=a_val,hatch='',label='Level 5')
circ4= mpatches.Patch( facecolor=colors[3],alpha=a_val,hatch='///',label='Level 6')
circ5 = mpatches.Patch(facecolor=colors[4],alpha=a_val,hatch='',label='Level 7-10')

font = 24

simplified_list=[]
simp_list=[]
# print("\n\nlist is\n\n",percentage)
for i in range(len(percentage[0])):
    sum_lv13=0
    sum_lv710=0
    simplified_list=[]
    for j in range(10):
        if(j>=0 and j<=2):
            sum_lv13=sum_lv13+percentage[i][j]
        elif(j>=6 and j<=9):
            sum_lv710=sum_lv710+percentage[i][j]
        else:
            simplified_list.insert((j-2),percentage[i][j])
    simplified_list.insert(0,sum_lv13)
    simplified_list.insert(4,sum_lv710)
    simp_list.append(simplified_list)

print("\n\nsimplified list\n\n",simp_list)

BM = [ "T1", "T2", "T3", "T4", "T5","T6"]
# percentage = [[87, 8, 5], [87, 8, 5], [87, 2, 10], [92, 7, 1],  [87, 2, 10] ]legend = ["Level 1", "Level 2", "Level 3", "Level 4","Level 5", "Level 6", "Level 7", "Level 8", "Level 9","Level 10"]
#plt.legend(legend, fontsize=font, loc='upper center', ncol = 2, frameon=True,
          # facecolor='w', edgecolor='k', fancybox=False, handletextpad=0.1, labelspacing=0, bbox_to_anchor=(0.5,1.3))
# percentage = [[75, 25],[75, 25],[65,34], [96 , 4], [65,34] ]
# percentage = [[66, 6, 4, 24 ], [66, 6, 4, 24 ], [ 66, 1.5, 6.5, 26 ], [89, 6.5 , 0.9, 3.6], [ 66, 1.5, 6.5, 26 ]]

fig,ax=plt.subplots(figsize=(10, 6))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(rotation=20 , rotation_mode = 'anchor', va="top", fontsize = font ,ha= 'right', color='k')
plt.yticks(fontsize = font, color='k')


width = 0.6

for (i, bm) in enumerate(BM):
    dataset = percentage[i]
    p1 = plt.bar(bm, dataset[0], width, color='#cce6ff')
    p2 = plt.bar(bm, dataset[1], width, bottom=dataset[0], color='#cce6ff', hatch='')
    p3 = plt.bar(bm, dataset[2], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]),  color='#cce6ff',  hatch='')
    p4 = plt.bar(bm, dataset[3], width, 
                bottom=(np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])), color='#ffeca9',  hatch='//'  )
    p5 = plt.bar(bm, dataset[4], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3]), color='#d099e2',  hatch=''  )
    p6 = plt.bar(bm, dataset[5], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4]), color='#ccd1f1',  hatch='//'  )
    p7 = plt.bar(bm, dataset[6], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[5]), color='#86ac3f',  hatch=''  )
    p8 = plt.bar(bm, dataset[7], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[5])+np.array(dataset[6]), color='#86ac3f',  hatch=''  )
    p9 = plt.bar(bm, dataset[8], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[5])+np.array(dataset[6])+np.array(dataset[7]), color='#86ac3f',  hatch=''  )
    p10 = plt.bar(bm, dataset[9], width, 
                bottom=np.array(dataset[1])+np.array(dataset[0]) + np.array(dataset[2])+np.array(dataset[3])+np.array(dataset[4])+np.array(dataset[5])+np.array(dataset[6])+np.array(dataset[7])+np.array(dataset[8]), color='#86ac3f', hatch='' )
    
    


# plt.title('Runtime Normalized To Hit_rate = 0', size =font)




plt.ylabel('Cache Occupancy', size = font, color='k')
plt.xlabel('Time Step', size = font, color='k')
# plt.xlabel('DSAs', size = font, color='k')
    
plt.tight_layout()
plt.savefig('./Plots/pdfs/multilevelidx.pdf')
plt.show()