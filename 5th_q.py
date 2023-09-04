import pandas as pd
import numpy as np 

import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/auto-mpg.csv")
print(data)

plt.hist(data['mpg'])

plt.scatter(data['mpg'],data['weight'])

plt.show()

output

mpg  cylinders  ...  origin                   car name
0    18.0          8  ...       1  chevrolet chevelle malibu
1    15.0          8  ...       1          buick skylark 320
2    18.0          8  ...       1         plymouth satellite
3    16.0          8  ...       1              amc rebel sst
4    17.0          8  ...       1                ford torino
..    ...        ...  ...     ...                        ...
393  27.0          4  ...       1            ford mustang gl
394  44.0          4  ...       2                  vw pickup
395  32.0          4  ...       1              dodge rampage
396  28.0          4  ...       1                ford ranger
397  31.0          4  ...       1                 chevy s-10

[398 rows x 9 columns]
