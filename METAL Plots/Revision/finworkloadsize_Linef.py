# matplotlib inline
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()





BM_name = ["10M","40M","80M","100M"]
x = np.linspace(4,len(BM_name),len(BM_name))
r40_64 = [6.17,5.93,5.72,5.41] #64K
r40_128 = [6.94,6.71,6.58,6.42] #128K
r40_256 = [7.13,7.03,6.91,6.72] #256K
r40_512 = [5.32,5.01,4.23,3.71] #512K

ax.plot (BM_name,[(r40_512[i]*5+(10-r40_512[i])*100) for i in range(len(r40_512))],marker="^",color="red")
ax.plot (BM_name,[(r40_64[i]*5+(10-r40_64[i])*100) for i in range(len(r40_64))],marker="o",color="blue")
ax.plot (BM_name,[(r40_128[i]*5+(10-r40_128[i])*100) for i in range(len(r40_128))],marker="v",color="orange")
ax.plot (BM_name,[(r40_256[i]*5+(10-r40_256[i])*100) for i in range(len(r40_256))],marker="x",color="green")


r40_64s = [6.17,4.34,3.01,2]
r40_128s= [6.94,4.96,3.18,3.07]
r40_256s = [7.13,5.43,5.06,4.34]
r40_512s = [5.36,3.27,2.07,1.41]

ax.plot (BM_name,[(r40_512s[i]*5+(10-r40_512s[i])*100) for i in range(len(r40_512s))],marker="^",linestyle="dotted",color="red",markerfacecolor="none")
ax.plot (BM_name,[(r40_64s[i]*5+(10-r40_64s[i])*100) for i in range(len(r40_64s))],marker="o",linestyle="dotted",color="blue",markerfacecolor="none")
ax.plot (BM_name,[(r40_128s[i]*5+(10-r40_128s[i])*100) for i in range(len(r40_128s))],marker="v",linestyle="dotted",color="orange",markerfacecolor="none")
ax.plot (BM_name,[(r40_256s[i]*5+(10-r40_256s[i])*100) for i in range(len(r40_256s))],marker="x",linestyle="dotted",color="green",markerfacecolor="none")


legend = ["32K Cache","64K Cache","128K Cache","256K Cache", "32K Cache S","64K Cache S","128K Cache S","256K Cache S"]
plt.legend(legend, fontsize=10, loc='best', ncol = 4, frameon=True,
           facecolor='w', edgecolor='k', fancybox=False, bbox_to_anchor=(1.2, 1.2))
plt.ylabel('Walk Latency', size=14, color='k')
plt.xlabel('Workload Size', size=14, color='k')
plt.savefig("Plots/pdfs/Workload_Linef_r40.pdf")
plt.show()