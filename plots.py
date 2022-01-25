# No of elements: 1000000
# degree: 5 (9 Nodes)
# Levels: 9
# 90% random
# Levels Saved: 31.02 %
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


y = np.array([64883, 29370, 26171, 86178, 287307, 355211, 113276, 37604])
Levels = ["2", "3", "4", "5", "6", "7", "8", "9"]

plt.pie(y, labels = Levels)
plt.show() 