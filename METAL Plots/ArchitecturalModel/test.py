import os
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
def read_file(path):
    f = open(path)
    lines = f.readlines()
    start = 3
    end = start + 10
    all = []
    for idx in range(10):
        n = []
        for l in lines[start:end]:
            n.append(int(l.strip().split(',')[-1].strip()))
        all.append(n)
        start+=13
        end+=13    


    return all

numbers = read_file('rand_sk.txt')

video = cv2.VideoWriter('video_sk100.avi', 0, 1, (640,480))

#define data
for t in range(10):
    plt.cla()
    data = numbers[t]
    # labels = ['1','2','3','4','5','6','7','8','9','10']
    labels=[]
    for idx,d in enumerate(data):
        if d<10000:
            labels.append('')
        else:
            labels.append(idx+1)
    # print(labels)
    #define Seaborn color palette to use
    colors = sns.color_palette('pastel')[0:5]
    print(data)
    #create pie chart
    plt.pie(data, labels = labels, colors = colors)
    plt.legend(title = "levels:", bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.title('Timestamp:  '+str(t+1))
    plt.savefig('test'+str(t)+'.png')
    video.write(cv2.imread('test'+str(t)+'.png'))

cv2.destroyAllWindows()
video.release()