# matplotlib inline
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

font = 30
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()





BM_name = ["10","12","15","18"]
x = np.linspace(4,len(BM_name),len(BM_name))
r80_64 = [5.34,5.78,6.92,8.47] #64K
r80_128 = [6.32,6.98,7.97,9.03] #128K
r80_256 = [6.96,8.06,9.13,11.19] #256K
r80_512 = [4.96,4.99,6.07,7.31]

r80_1281=[0,0,0,0]
r80_2561=[0,0,0,0]
r80_5121=[0,0,0,0]
r80_641=[0,0,0,0]

for i in range(len(r80_128)):
    if(i==0):
        r80_641[i]=10-r80_64[i]
        r80_1281[i]=10-r80_128[i]
        r80_2561[i]=10-r80_256[i]
        r80_5121[i]=10-r80_512[i]
    elif(i==1):
        r80_641[i]=12-r80_64[i]
        r80_1281[i]=12-r80_128[i]
        r80_2561[i]=12-r80_256[i]
        r80_5121[i]=12-r80_512[i]
    elif(i==2):
        r80_641[i]=15-r80_64[i]
        r80_1281[i]=15-r80_128[i]
        r80_2561[i]=15-r80_256[i]
        r80_5121[i]=15-r80_512[i]
    else:
        r80_641[i]=18-r80_64[i]
        r80_1281[i]=18-r80_128[i]
        r80_2561[i]=18-r80_256[i]
        r80_5121[i]=18-r80_512[i]


fig, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor('w')
ax.set_axisbelow(True)
ax.spines['bottom'].set_color('k')
plt.grid(linestyle='--', linewidth=2, which='major', color='darkgray')
plt.gca().xaxis.grid(False)
plt.gca().yaxis.grid(True)

# ax.tick_params(axis='y', which='minor', left=False)
# plt.tick_params(axist='both', which='major', direction='in', length=6, width=3)
# plt.xticks(X_AXIS, ha='center', color='k', rotation=10)
plt.xticks(size=font, va="top")
plt.yticks(fontsize=font, color='k')


# xticks_minor = [0]
# ax.set_xticks(xticks_minor, minor=True)

# ax.tick_params(axis='x', which='minor', direction='out', length=10, width=1)

plt.yticks(fontsize=font, color='k')

ax.set_xticklabels(BM_name)

plt.plot(BM_name,[(r80_512[i]*5+r80_5121[i]*100) for i in range(len(r80_512))],marker="^",color="red",linewidth=5,markersize=20)
plt.plot (BM_name,[(r80_64[i]*5+r80_641[i]*100) for i in range(len(r80_64))],marker="o",color="blue",linewidth=5,markersize=20)
plt.plot (BM_name,[(r80_128[i]*5+r80_1281[i]*100) for i in range(len(r80_128))],marker="v",color="orange",linewidth=5,markersize=20)
plt.plot (BM_name,[(r80_256[i]*5+r80_2561[i]*100) for i in range(len(r80_256))],marker="s",color="green",linewidth=5,markersize=20)



# legend = ["32K","64K","128K","256K"]
# plt.legend(legend, fontsize=font, loc='best', ncol = 4, frameon=True,
#            facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.9, 1.1))
plt.ylabel('Walk Latency', size=font, color='k')
plt.xlabel('IDX Depth', size=font, color='k')

plt.tight_layout()
plt.savefig("Plots/pdfs/vary_depth_r80.pdf")
# plt.show()