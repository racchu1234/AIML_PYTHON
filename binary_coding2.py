import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/Book11.csv")
print(data)
d1=pd.DataFrame(data,columns=["marks","sex"])
print(d1)
print()
df1=pd.get_dummies(d1["sex"])
print(df1)
print()
df2=pd.concat((df1,d1),axis=1)
print(df2)
print()
df3=df2.drop(["sex"],axis=1)
print(df3)
print()
df4=df2.drop(["marks"],axis=1)
print(df4)
result=df2.rename(columns={"sex":"gender"})
print(result)

output

school sex  age address famsize Pstatus  marks
0      GP   F   18       U     GT3       A     10
1     GPq   F   17       U     GT3       T     10
2       l   F   15       U     LE3       T     20
3     Gpi   F   15       U     GT3       T     25
4     Gpu   F   16       U     GT3       T     30
5      GP   M   16       U     LE3       T     40
6       y   M   16       U     LE3       T     50
7       j   F   17       U     GT3       A     60
8       k   M   15       U     LE3       A     66
9       u   M   15       U     GT3       T     66
10      t   F   15       U     GT3       T     55
11      c   F   15       U     GT3       T     44
12      t   M   15       U     LE3       T     33
13      v   M   15       U     GT3       T     55
14     GP   M   15       U     GT3       A     66
15      n   F   16       U     GT3       T     88
16     mj   F   16       U     GT3       T     99
17      j   F   16       U     GT3       T     11
18      y   M   17       U     GT3       T     22
19      r   M   16       U     LE3       T     44
    marks sex
0      10   F
1      10   F
2      20   F
3      25   F
4      30   F
5      40   M
6      50   M
7      60   F
8      66   M
9      66   M
10     55   F
11     44   F
12     33   M
13     55   M
14     66   M
15     88   F
16     99   F
17     11   F
18     22   M
19     44   M

    F  M
0   1  0
1   1  0
2   1  0
3   1  0
4   1  0
5   0  1
6   0  1
7   1  0
8   0  1
9   0  1
10  1  0
11  1  0
12  0  1
13  0  1
14  0  1
15  1  0
16  1  0
17  1  0
18  0  1
19  0  1

    F  M  marks sex
0   1  0     10   F
1   1  0     10   F
2   1  0     20   F
3   1  0     25   F
4   1  0     30   F
5   0  1     40   M
6   0  1     50   M
7   1  0     60   F
8   0  1     66   M
9   0  1     66   M
10  1  0     55   F
11  1  0     44   F
12  0  1     33   M
13  0  1     55   M
14  0  1     66   M
15  1  0     88   F
16  1  0     99   F
17  1  0     11   F
18  0  1     22   M
19  0  1     44   M

    F  M  marks
0   1  0     10
1   1  0     10
2   1  0     20
3   1  0     25
4   1  0     30
5   0  1     40
6   0  1     50
7   1  0     60
8   0  1     66
9   0  1     66
10  1  0     55
11  1  0     44
12  0  1     33
13  0  1     55
14  0  1     66
15  1  0     88
16  1  0     99
17  1  0     11
18  0  1     22
19  0  1     44

    F  M sex
0   1  0   F
1   1  0   F
2   1  0   F
3   1  0   F
4   1  0   F
5   0  1   M
6   0  1   M
7   1  0   F
8   0  1   M
9   0  1   M
10  1  0   F
11  1  0   F
12  0  1   M
13  0  1   M
14  0  1   M
15  1  0   F
16  1  0   F
17  1  0   F
18  0  1   M
19  0  1   M
    F  M  marks gender
0   1  0     10      F
1   1  0     10      F
2   1  0     20      F
3   1  0     25      F
4   1  0     30      F
5   0  1     40      M
6   0  1     50      M
7   1  0     60      F
8   0  1     66      M
9   0  1     66      M
10  1  0     55      F
11  1  0     44      F
12  0  1     33      M
13  0  1     55      M
14  0  1     66      M
15  1  0     88      F
16  1  0     99      F
17  1  0     11      F
18  0  1     22      M
19  0  1     44      M
