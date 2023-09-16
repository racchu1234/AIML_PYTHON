import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data1=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/stu_id.csv")
print(data1)
data2=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/stu_mar.csv")
print(data2)
data3=pd.merge(data1,data2)
print(data3)
print(data3.head(10))

number=pd.DataFrame({"number":[100,200,300,200,500,600,600,800,900,120]})
print(number)
roll=pd.DataFrame({"roll":[88,66,77,99,55,44,33,22,55,66]})
print(roll)
print(roll.shape)
add=data1.assign(number=number,roll=roll)
print(add.head(10))

dat=roll.duplicated(subset=None,keep="last").sum()
print(dat)

da=number.drop_duplicates(subset=None,keep="first")
print(da)
print(da.shape)

new=data1.insert(1,"number",number)
print(new)

m=number.assign(percentage=list(map(lambda x:x*100/500,number["number"])))
print(m)

output

student name  sid
0           abc    1
1           cde    2
2           fgh    8
3            ik    3
4           lmn    5
5           opq    4
6           rst    6
7           uvw    7
8           xyz    9
9          neha   10
10       poorna   11
11       rukiya   12
12       anudra   13
13     jagruthi   14
14      inchara   15
15       ananya   16
16       nithya   17
17       swetha   18
18    sangeetha   19
19     ruchitha   20
20        shree   21
21        thanu   22
22    harshitha   23
23     parvathi   24
24    nagashree   25
25   nivedhitha   26
26    rakshitha   27
27        varun   28
28       likith   29
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
   student name  sid  marks
0           abc    1     96
1           cde    2     98
2           fgh    8     75
3            ik    3     86
4           lmn    5     53
5           opq    4     96
6           rst    6      9
7           uvw    7      1
8           xyz    9     78
9          neha   10     75
10       poorna   11     63
11       rukiya   12     62
12       anudra   13     36
13     jagruthi   14     60
14      inchara   15     21
15       ananya   16     55
16       nithya   17     54
17       swetha   18     50
18    sangeetha   19     32
19     ruchitha   20     36
20        shree   21      9
21        thanu   22     77
22    harshitha   23     74
23     parvathi   24      7
24    nagashree   25     50
25   nivedhitha   26     60
26    rakshitha   27     22
27        varun   28     88
28       likith   29     66
  student name  sid  marks
0          abc    1     96
1          cde    2     98
2          fgh    8     75
3           ik    3     86
4          lmn    5     53
5          opq    4     96
6          rst    6      9
7          uvw    7      1
8          xyz    9     78
9         neha   10     75
   number
0     100
1     200
2     300
3     200
4     500
5     600
6     600
7     800
8     900
9     120
   roll
0    88
1    66
2    77
3    99
4    55
5    44
6    33
7    22
8    55
9    66
(10, 1)
  student name  sid  number  roll
0          abc    1   100.0  88.0
1          cde    2   200.0  66.0
2          fgh    8   300.0  77.0
3           ik    3   200.0  99.0
4          lmn    5   500.0  55.0
5          opq    4   600.0  44.0
6          rst    6   600.0  33.0
7          uvw    7   800.0  22.0
8          xyz    9   900.0  55.0
9         neha   10   120.0  66.0
2
   number
0     100
1     200
2     300
4     500
5     600
7     800
8     900
9     120
(8, 1)
None
   number  percentage
0     100        20.0
1     200        40.0
2     300        60.0
3     200        40.0
4     500       100.0
5     600       120.0
6     600       120.0
7     800       160.0
8     900       180.0
9     120        24.0
