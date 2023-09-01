import pandas as pd
import numpy as np 

import matplotlib.pyplot as pl

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/taitanic.csv")
print(data)
pl.plot(data['Age'])
pl.plot(data['Fare'])
pl.xlabel("Age")
pl.ylabel('Fare')
pl.show()

output

      Passengerid   Age      Fare  Sex  ...  Embarked  zero.17  zero.18  2urvived
0               1  22.0    7.2500    0  ...       2.0        0        0         0
1               2  38.0   71.2833    1  ...       0.0        0        0         1
2               3  26.0    7.9250    1  ...       2.0        0        0         1
3               4  35.0   53.1000    1  ...       2.0        0        0         1
4               5  35.0    8.0500    0  ...       2.0        0        0         0
          ...   ...       ...  ...  ...       ...      ...      ...       ...
1304         1305  28.0    8.0500    0  ...       2.0        0        0         0
1305         1306  39.0  108.9000    1  ...       0.0        0        0         0
1306         1307  38.5    7.2500    0  ...       2.0        0        0         0
1307         1308  28.0    8.0500    0  ...       2.0        0        0         0
1308         1309  28.0   22.3583    0  ...       0.0        0        0         0

[1309 rows x 28 columns]
