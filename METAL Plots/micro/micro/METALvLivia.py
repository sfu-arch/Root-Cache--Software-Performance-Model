# matplotlib inline
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
import numpy as np
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
fig = plt.figure()
ax = plt.axes()

mpl.rc('font', family='sans-serif')
matplotlib.style.use('ggplot')

font = 34
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)



BM_name = ["10M","40M","80M","100M"]
x = np.linspace(4,len(BM_name),len(BM_name))
r80_64 = [5.34,5.21,4.96,4.18] #64K
livia_1l = [2.46, 2.13, 2.04, 2.18]
livia_l2 = [4.16, 3.12, 2.32, 1.06]
r80_128 = [6.32,6.11,5.97,5.56] #128K
r80_256 = [6.96,6.87,6.73,6.59] #256K
r80_512 = [4.21,3.97,2.69,1.79]#512K

# X_AXIS = np.linspace(1.5, len(BM_name), len(BM_name))

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

# ax.tick_params(axis='y', which='minor', left=False)
# plt.tick_params(axis='both', which='major', direction='in', length=6, width=3)
# plt.xticks(X_AXIS, ha='center', color='k', rotation=10)
plt.xticks(size=font, va="top")
plt.yticks(fontsize=font, color='k')


# xticks_minor = [0]
# ax.set_xticks(xticks_minor, minor=True)

# ax.tick_params(axis='x', which='minor', direction='out', length=10, width=1)

plt.yticks(fontsize=font, color='k')

ax.set_xticklabels(BM_name)

# ax.plot (BM_name,[(r80_512[i]*5+(10-r80_512[i])*100) for i in range(len(r80_512))],marker="^",color="red",markersize=20,linewidth=5)
ax.plot (BM_name,[(r80_64[i]*4+(10-r80_64[i])*100) for i in range(len(r80_64))],marker="o",color="blue",markersize=20,linewidth=5)
ax.plot (BM_name,[(livia_1l[i]*1 + livia_l2[i]*2 +(10-(livia_1l[i] + livia_l2[i]))*100) for i in range(len(r80_64))],marker="o",color="orange",markersize=20,linewidth=5)
# ax.plot (BM_name,[(r80_128[i]*5+(10-r80_128[i])*100) for i in range(len(r80_128))],marker="v",color="orange",markersize=20,linewidth=5)
# ax.plot (BM_name,[(r80_256[i]*5+(10-r80_256[i])*100) for i in range(len(r80_256))],marker="s",color="green",markersize=20,linewidth=5)

r80_64s = [5.34,3.14,2.76,2.34]
r80_128s= [6.32,4.91,3.96,3.01]
r80_256s = [6.96,5.12,4.93,4.06]
r80_512s = [4.21,2.06,1.34,1.04]

# ax.plot (BM_name,[(r80_512s[i]*5+(10-r80_512s[i])*100) for i in range(len(r80_512s))],marker="^",linestyle="dotted",color="red",markerfacecolor="none",markersize=20,linewidth=5)
ax.plot (BM_name,[(r80_64s[i]*5+(10-r80_64s[i])*100) for i in range(len(r80_64s))],marker="o",linestyle="dotted",color="blue",markerfacecolor="none",markersize=20,linewidth=5)
# ax.plot (BM_name,[(r80_128s[i]*5+(10-r80_128s[i])*100) for i in range(len(r80_128s))],marker="v",linestyle="dotted",color="orange",markerfacecolor="none",markersize=20,linewidth=5)
# ax.plot (BM_name,[(r80_256s[i]*5+(10-r80_256s[i])*100) for i in range(len(r80_256s))],marker="s",linestyle="dotted",color="green",markerfacecolor="none",markersize=20,linewidth=5)


legend = ["64K","64K++", "Livia-2L"]
# plt.legend(legend, fontsize=font, loc='best', ncol = 8, frameon=True,
# facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1.1, 1.18))
plt.ylabel('Walk Latency', size=font, color='k')
plt.xlabel('Workload Size', size=font, color='k')

# plt.tight_layout()

plt.savefig("pdfs/METALvLivia.jpeg")
plt.show()