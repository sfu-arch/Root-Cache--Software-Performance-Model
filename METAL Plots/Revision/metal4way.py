# import matplotlib.pyplot as plt
   
# Year = [32,64,128,256,512,1024]
# AddressBasedCache = [7.30670, 6.96743, 6.54331, 5.02799, 4.63410, 4.24477]
# Indexcache = [8.71248, 7.02411, 6.43178, 4.60211, 3.10420, 2.41270]
  
# line1, = plt.plot(Year, AddressBasedCache, 'x-')
# line2, = plt.plot(Year, Indexcache, '+-')
# plt.title('Index Cache Vs Address Based Cache')
# plt.xlabel('Cache Size in ')
# plt.ylabel('Latency (in cycles)')
# plt.legend(["Address Cache", "Index Cache"])
# plt.savefig('ICvAC_seq.png')
# plt.show()

import sys

import math


import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib
from matplotlib.transforms import Bbox
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator
from random import randint
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.ticker as ticker
import csv


mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')


font = 16
Year = [4,8,16,32,64,128,256]
way4 = [0.52, 0.71,0.77,1.03,1.21,1.97,2.83]
metal = [1.93,2.11,2.27,3.31,4.51,5.13,6.77]

fig,ax=plt.subplots(figsize=(6, 5))
line1, = plt.plot(Year, way4, 'o-',linewidth=3,markersize=15,color="blue")
line2, = plt.plot(Year, metal, 'v-',linewidth=3,markersize=15,color="red")
# line3, = plt.plot(Year, locality, '*-',linewidth=3,markersize=20,color="green")
ax.set_facecolor('w')
ax.set_axisbelow(True)

    
print(metal)
print(way4)

ax.tick_params(axis='y', which='minor', left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)

plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='k')

ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)
plt.xlabel('Cache size (kB)',size=font, color='k')
plt.ylabel('Norm. Speed Up', size=font, color='k')
plt.legend(["4-way address cache", " METAL"],fontsize=16,loc='upper left',fancybox=False,edgecolor='k',bbox_to_anchor=(-0.175, 1.2),ncol=3)
plt.savefig('Plots/pdfs/metal4way.pdf')
plt.show()