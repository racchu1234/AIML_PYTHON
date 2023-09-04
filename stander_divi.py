import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/taitanic.csv")
print(pd.DataFrame(data))
print(data['Age'].mean())
print(data.median())
print(data.mode())
print(data['Age'].mode())

speed=[1,2,3,4,5,6,7,8,9,3,6,3,4,3,3,3,3]
r=np.std(speed)
print(r)
print(len(speed))

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
29.50318563789152
Passengerid    655.0000
Age             28.0000
Fare            14.4542
Sex              0.0000
sibsp            0.0000
zero             0.0000
zero.1           0.0000
zero.2           0.0000
zero.3           0.0000
zero.4           0.0000
zero.5           0.0000
zero.6           0.0000
Parch            0.0000
zero.7           0.0000
zero.8           0.0000
zero.9           0.0000
zero.10          0.0000
zero.11          0.0000
zero.12          0.0000
zero.13          0.0000
zero.14          0.0000

