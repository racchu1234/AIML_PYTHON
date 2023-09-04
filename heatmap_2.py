import numpy as npy

import seaborn as sbn

import matplotlib.pyplot as plt

data = npy.random.randint(low = 1, high = 100, size = (10, 10))

print("To be plotted:\n")

print(data)

hm = sbn.heatmap(data = data)

plt.show()

output

To be plotted:

[[91 46 74 34 97 97 34 61 94 14]
 [72 98 90 96 70  6 14 42 36 28]
 [80 88 92 55 84 13 98 34 61 21]
 [33 56  2 12 18 45  5 50 71 57]
 [81 40  5 52 42 13 12 93 45 77]
 [29 63 83 56 32  9  4 97  7 67]
 [67 86 20 16 61 69 70 79 44 15]
 [ 2 10 42 47 93 24 40 48  8 35]
 [16 66 76 29 52 40 14 83 85 84]
 [25 59 31 33  2  5  5 42 15 61]]
