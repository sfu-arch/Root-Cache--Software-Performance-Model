import sys

import math
from scipy.stats import gmean



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

font = 24
X_AXIS_name = []
X_AXIS = np.linspace(0.1, 0.9, 9)




stream =[]
metal=[]
cache =[]

font = 20

BM_name = ['Scan 40%' , "WHERE", "JOIN","Nest.SEL","RTree","PageRank","SpMM","SpMM-S.","KVStore","KVStore-S","G.MEAN"]
# stream =     ([12.62, 9.31, 8.21 , 2.36, 4.96,13.42,18.33,21.42, 10.06,22.46,17.89,1])
# cache = ([7.28, 7.17, 7.03, 1.81, 3.03,10.79,14.08,19.76,7.83,20.62,11.32,0])
# metal = (([5.17, 2.54, 1.83 , 1.15, 1.08,5.96,9.62,11.31,2.26,15.16,6.13,0]))
# xcache = (([7.06, 7.04, 6.93 , 1.74, 1.17,8.37,13.78,18.27,4.78,19.96,9.78,0]))
stream = ([8.21,18.33,21.42,13.42,22.46,17.89,10.06,4.96,2.36,2.36,1])
cache = ([7.03,14.08,19.76,10.79,20.62,11.32,7.83,4.96,1.81,2.67,0])
metal = (([1.83,9.62,11.31,5.96,15.16/1.17,6.13,2.26,4.96,1.15,2.36,0]))
metalix = (([1.83,9.62,11.31,5.96,15.16/1.17,6.13,2.26,4.96,1.15,2.6,0]))
xcache = (([6.93,13.78,18.27,8.37,19.96,9.78,4.78,4.96,1.74,2.36,0]))
scaling=([1,3.17,4.32,3.62])

X_AXIS = np.linspace(1,len(BM_name),len(BM_name))


fig,ax=plt.subplots(figsize=(18, 4.4))
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


xticks_minor = [3.5,6.5,8.5, 10.6 ]

ax.set_xticks( xticks_minor, minor=True )

ax.tick_params( axis='x', which='minor', direction='out', length=40, width =3 )
plt.yticks(fontsize = font, color='k')

ax.set_xticklabels(BM_name)
prod=1
met=([ 0 , 0, 0,0,0, 0,0,0,0,0])
metix=([ 0 , 0, 0,0,0, 0,0,0,0,0])
xc1=([ 0 , 0, 0,0,0, 0,0,0,0,0])
fa1=([0 , 0, 0,0,0, 0,0,0,0,0])

for i in range(1,4):
        metal[i]=metal[i]/1.37
        metalix[i]=metalix[i]/1.37
        xcache[i]=xcache[i]*1.36
       
for i,X in  enumerate(stream):
    if(i==10):
        break
    met[i] = (X/(metal[i]))*0.87*scaling[2]
    metix[i] = (X/(metalix[i]))*0.87*scaling[2]
    xc1[i]= (X/xcache[i])*0.9*scaling[3]
    fa1[i] = (X/(cache[i]))*0.74*scaling[1]
    
geomean=math.pow(prod,len(stream))
print("trial",geomean)

#calculate geometric mean
metal[-1]=scaling[2]/(gmean(met))
metalix[-1]=scaling[2]/(gmean(metix))
cache[-1]=scaling[1]/(gmean(fa1))
xcache[-1]=scaling[3]/(gmean(xc1))

print("by 1")
print(metal[-1])
print(stream[-1])

# for i in range(1,4):
#         metal[i]=metal[i]/1.37
#         metalix[i]=metalix[i]/1.37
#         xcache[i]=xcache[i]*1.36
       

summ=0
plt.bar([i - 0.31 for i in X_AXIS], [(X/((metal[i]))) *0.87*scaling[2] for i,X in  enumerate(stream)], hatch = "//", width  = 0.15, color = "#e9e9e9")
plt.bar([i - 0.15 for i in X_AXIS], [(X/((metalix[i])*1.47)) *0.87*scaling[2] for i,X in  enumerate(stream)], width  = 0.15, color = "#e3e3e3")
plt.bar([i + 0.01 for i in X_AXIS], [(X/xcache[i])*0.9*scaling[3] for i,X in  enumerate(stream)], hatch = ".", width  = 0.15, color = "gray")
plt.bar([i + 0.16 for i in X_AXIS], [(X/(cache[i]))*0.74*scaling[1] for i,X in  enumerate(stream)], width  = 0.15, color = "#b1b1b1")
plt.bar([i + 0.31 for i in X_AXIS], [(X/stream[i])*scaling[0] for i,X in  enumerate(stream)], hatch = "//", width  = 0.15, color = "black")
for i in range(len(cache)):
    summ = summ + (stream[i]/metal[i])
print()
print()
avg=(summ*scaling[2])/(11*scaling[0])
print("avg is",avg)

#geometric mean

# prod=1
# met=([0, 0, 0 , 0, 0,0,0, 0,0,0])
# xc1=([0, 0, 0 , 0, 0,0,0, 0,0,0])
# fa1=([0, 0, 0 , 0, 0,0,0, 0,0,0])
# for i,X in  enumerate(stream-1):
#     met[i] = (X/metal[i])*scaling[2]
#     xc1[i]= (X/xcache[i])*scaling[3]
#     fa1[i] = (X/cache[i])*scaling[1]
    
# geomean=math.pow(prod,len(stream))
# print("trial",geomean)

# #calculate geometric mean
print("geomeans")
print(metal[-1])
print(cache[-1])
print(xcache[-1])
print("stream/value")
print(stream[-1]/metal[-1])
print("by 1")
print(scaling[2]/metal[-1])
# plt.plot(0, y, '-r', label='y=2x+1')
with open('hbm_Values', 'w') as f:
    # f.writelines(lines)

    f.write("metal:\n")

    for i in range(len(metal)):
        f.write(str((stream[i]/metal[i])*scaling[2]))
        f.write("\n")
    f.write("cache:\n")
    for i in range(len(cache)):
        f.write(str((stream[i]/cache[i])*scaling[1]))
        f.write("\n")
    f.write("stream:\n")
    for i in range(len(stream)):
        f.write(str((stream[i]/stream[i])*scaling[0]))
        f.write("\n")
f.close()
# plt.bar([i - 0.20 for i in X_AXIS], [X/metal[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "black", height=1.6)
# plt.bar([i + 0.05 for i in X_AXIS], [X/cache[i] for i,X in  enumerate(stream)], hatch = "||", width  = 0.2, color = "#C5C5C5", height=1.6)
# plt.bar([i + 0.25 for i in X_AXIS], [X/stream[i] for i,X in  enumerate(stream)], hatch = "--", width  = 0.2, color = "#D3D3D3", height=1.6)

# plt.title('Runtime Comparision', size =font)
legend = ["METAL","METAL-IX","X-Cache", "Addr", "Stream"]
plt.legend(legend, fontsize=18, loc='best', ncol = 5, frameon=True,handletextpad=0.05,columnspacing=0.39,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(0.1, 0.98))
# plt.axhline(geom, color = 'r', linestyle = 'dotted',linewidth=2)

plt.ylabel('Norm. Speedup', size = font, color='k')
# plt.ylim([0,25])
# plt.xlabel('Benchmark', size = font, color='k')

plt.annotate("Gorgon",     (0.14,-0.12), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')

# plt.annotate("Wid-X",(0.27,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font ,weight='bold')
# plt.annotate("Capstan",   (0.35,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
# plt.annotate("Aurochs",   (0.42,-0.2), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Aurochs",   (0.395,-0.12), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Capstan",   (0.585,-0.12), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.annotate("Wid-X",   (0.77,-0.12), xycoords='axes fraction', textcoords='offset points', va='top', size = font,weight='bold')
plt.tight_layout()
# Uncomment to savefig
plt.savefig('./Plots/pdfs/Performance_HBM.pdf')
print("xcache:",xcache[-1])
print("addr:",cache[-1])
print("stream",stream[-1])

print("geomeans:")

metal[-1]=(1/metal[-1])*0.87*scaling[2]
metalix[-1]=(1/((metalix[-1])*1.47)) *0.87*scaling[2]
xcache[-1]=(1/xcache[-1])*0.9*scaling[3] 
cache[-1]=(1/(cache[-1]))*0.74*scaling[1] 
stream[-1]=(1/stream[-1])*scaling[0]

print("Metal","metalix","xcache","cache","stream")
print(metal[-1],metalix[-1],xcache[-1],cache[-1],stream[-1])


# plt.show()