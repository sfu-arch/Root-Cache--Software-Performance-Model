


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

percentage = read_file("ran_stack.txt")

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

font = 24


BM = [ "B+Tree", "Hash Table", "SpMv", "Data Analytics", "SpMM"]

fig,ax=plt.subplots(figsize=(10, 7))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(rotation=20 , rotation_mode = 'anchor', size=font, va="top", fontsize = font ,ha= 'right', color='k')
plt.yticks(fontsize = font, color='k')

    

width = 0.4

for (i, bm) in enumerate(BM):
    dataset = percentage[i]
    p1 = plt.bar(bm, dataset[0]*100, width, color='black')
    p2 = plt.bar(bm, dataset[1]*100, width, bottom=dataset[0]*100, color='#d5d5d5', hatch='//')
   

legend = ["Wasted", "Useful"]
plt.legend(legend, fontsize=font, loc='upper center', ncol = 2, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, handletextpad=0.1, labelspacing=0, bbox_to_anchor=(0.5,1.1))
           

plt.ylabel('Evictions (%)', size = font, color='k')
plt.xlabel('Benchmarks', size = font, color='k')
# plt.xlabel('DSAs', size = font, color='k')
    
plt.tight_layout()
plt.savefig('./wastedEntries.pdf')
plt.show()