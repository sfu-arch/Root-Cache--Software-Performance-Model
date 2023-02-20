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

font = 36
X_AXIS_name = []
# X_AXIS = np.linspace(0.1, 0.9, 9)




stream =[]
metal=[]
cache =[]

font = 24

BM_name = ["10M","40M","80M","100M"]
cache = [6.17,5.93,5.72,5.41] #64K
metal = [6.94,6.71,6.58,6.42] #128K


X_AXIS = np.linspace(4,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(22, 9))
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
plt.ylabel('Norm. Utilisation (%)', size = font, color='k')
plt.xlabel('Levels ', size = font, color='k')


ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)
# plt.bar([i for i in X_AXIS], [100*cache[i] for i,X in  enumerate(cache)], hatch = "||", width  = 0.2, color = "black")
legend = ["Utilisation"]
plt.legend(legend, fontsize=font, loc='best', ncol = 1, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 1.11))
# ax2 = ax.twinx()

plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(False)

# ax2.tick_params(axis='y',which='minor',color='white',left=False)
plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
plt.xticks(X_AXIS ,ha= 'center', color='k', rotation = 20)
plt.xticks(size=font, va="top")
plt.yticks(fontsize = font, color='red')

# plt.bar([i - 0.20 for i in X_AXIS], [stream[i]/X for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black")

for i in range(4):
    cache[i]=cache[i]*5+(10-cache[i])*100
    metal[i]=metal[i]*5+(10-metal[i])*100

plt.plot(BM_name, [cache[i] for i in range(len(cache))], marker='o', color='red',markersize=20)
plt.plot(BM_name, [metal[i] for i in range(len(metal))], marker='v', color='blue',markersize=20)





# ax.plot([i for i in X_AXIS],[np.sin(i) for i in  enumerate(X_AXIS)]);

# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["64K Cache","128K Cache"]
plt.legend(legend, fontsize=font, loc='best', ncol = 2, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.8, 0.9))
plt.ylabel('Walk Latency', size = font, color='red')

plt.xlabel('Levels ', size = font, color='k')
# plt.xlabel('\n\n DSAs', size = font, color='k')

plt.tight_layout()
# Uncomment to savefig
plt.savefig('./workloadSize.pdf')
plt.show()



























