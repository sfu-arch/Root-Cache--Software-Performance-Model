import os
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
import numpy as np
def read_file(path):
    f = open(path)
    lines = f.readlines()
    start = 2
    end = start + 10
    all = []
    for idx in range(10):
        n = []
        for l in lines[start:end]:
            print(l.strip())
            n.append(int(l.strip()))
        all.append(n)
        start+=13
        end+=13    


    return all

numbers = read_file('ran_stack.txt')
fig, ax = plt.subplots()
#define data
labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10']
numbers= np.array(numbers)
Level_0 = np.array(numbers[:,0])
Level_1 = np.array(numbers[:,1])
Level_2 = np.array(numbers[:,2])
Level_3 = np.array(numbers[:,3])
Level_4 = np.array(numbers[:,4])
Level_5 = np.array(numbers[:,5])
Level_6 = np.array(numbers[:,6])
Level_7 = np.array(numbers[:,7])
Level_8 = np.array(numbers[:,8])
Level_9 = np.array(numbers[:,9])



width = 0.35 
ax.bar(labels, Level_0, width, label='Level_0')
ax.bar(labels, Level_1, width,
       label='Level_1', bottom=Level_0)
ax.bar(labels, Level_2, width,
       label='Level_2', bottom=Level_1 + Level_0)
ax.bar(labels, Level_3, width,
       label='Level_3', bottom=Level_1 + Level_0 + Level_2)
ax.bar(labels, Level_4, width,
       label='Level_4', bottom=Level_1 + Level_0 + Level_2 + Level_3)
ax.bar(labels, Level_5, width,
       label='Level_5', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4)
ax.bar(labels, Level_6, width,
       label='Level_6', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5)
ax.bar(labels, Level_7, width,
       label='Level_7', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6)
ax.bar(labels, Level_8, width,
       label='Level_8', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6 + Level_7)
ax.bar(labels, Level_9, width,
       label='Level_9', bottom=Level_1 + Level_0 + Level_2 + Level_3 + Level_4 + Level_5 + Level_6 + Level_7 + Level_8)

ax.set_ylabel('Cache Occupancy')
ax.set_xlabel('Time Step')
ax.set_title('Random Root Cache Snapshot')
ax.legend()
plt.savefig('test2r.png')

