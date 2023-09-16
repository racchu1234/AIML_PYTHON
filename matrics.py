import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/stu_mar.csv")
print(data)
x=data['marks'].values.reshape(-1,1)
print(x)
y=data['sid'].values.reshape(-1,1)
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=(0.2),random_state=4)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


from sklearn.linear_model import LinearRegression

lm=LinearRegression()
lm.fit(x_train,y_train)
ypredict=lm.predict(x_test)
print(ypredict)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

actual=y_test.reshape(2,3)
predict=ypredict.reshape(2,3)
mpe=mean_absolute_error(actual,predict)
hse=mean_squared_error(actual,predict)
rmsk=np.sqrt(mean_absolute_error(actual,predict))
r2=r2_score(actual,predict)

output

sid  marks
0     1     96
1     2     98
2     8     75
3     3     86
4     5     53
5     4     96
6     6      9
7     7      1
8     9     78
9    10     75
10   11     63
11   12     62
12   13     36
13   14     60
14   15     21
15   16     55
16   17     54
17   18     50
18   19     32
19   20     36
20   21      9
21   22     77
22   23     74
23   24      7
24   25     50
25   26     60
26   27     22
27   28     88
28   29     66
[[96]
 [98]
 [75]
 [86]
 [53]
 [96]
 [ 9]
 [ 1]
 [78]
 [75]
 [63]
 [62]
 [36]
 [60]
 [21]
 [55]
 [54]
 [50]
 [32]
 [36]
 [ 9]
 [77]
 [74]
 [ 7]
 [50]
 [60]
 [22]
 [88]
 [66]]
[[ 1]
 [ 2]
 [ 8]
 [ 3]
 [ 5]
 [ 4]
 [ 6]
 [ 7]
 [ 9]
 [10]
 [11]
 [12]
 [13]
 [14]
 [15]
 [16]
 [17]
 [18]
 [19]
 [20]
 [21]
 [22]
 [23]
 [24]
 [25]
 [26]
 [27]
 [28]
 [29]]
[[50]
 [60]
 [36]
 [96]
 [86]
 [54]
 [63]
 [ 9]
 [36]
 [75]
 [53]
 [74]
 [60]
 [ 1]
 [75]
 [32]
 [66]
 [78]
 [98]
 [96]
 [ 7]
 [21]
 [22]]
[[62]
 [77]
 [88]
 [55]
 [ 9]
 [50]]
[[18]
 [26]
 [20]
 [ 1]
 [ 3]
 [17]
 [11]
 [ 6]
 [13]
 [ 8]
 [ 5]
 [23]
 [14]
 [ 7]
 [10]
 [19]
 [29]
 [ 9]
 [ 2]
 [ 4]
 [24]
 [15]
 [27]]
[[12]
 [22]
 [28]
 [16]
 [21]
 [25]]
[[12.63815608]
 [10.92559344]
 [ 9.66971416]
 [13.43735199]
 [18.68921077]
 [14.0082062 ]]
