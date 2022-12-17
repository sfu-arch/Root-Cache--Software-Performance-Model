import matplotlib.pyplot as plt
import numpy as np

font=16
btree = np.array([30560,
54330,
28970])

analy=np.array([232190,
142350,
35090])
# labels=['Compute','IX-Cache','Pattern Controller']
colour=['#fdb73e','#7a77e6','#4adede']
plt.pie(analy, autopct='%1.1f%%',colors=colour,textprops={'fontsize': font})
plt.savefig('Plots/pdfs/energy_analytics.pdf')
plt.show()