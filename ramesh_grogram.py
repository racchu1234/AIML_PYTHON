import pandas as pd
data=pd.DataFrame({"Days":[1,2,3,4,5,6,7,8,9,10],
                   "steps":[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]})
print(data)
df=pd.DataFrame(data)
df['steps']= df['steps']+1000
print(df)
   
a=df[df['steps']>7000] ['Days']
print(list(a))

output

Days  steps
0     1   4335
1     2   9552
2     3   7332
3     4   4504
4     5   5335
5     6   7552
6     7   8332
7     8   6504
8     9   8965
9    10   7689
   Days  steps
0     1   5335
1     2  10552
2     3   8332
3     4   5504
4     5   6335
5     6   8552
6     7   9332
7     8   7504
8     9   9965
9    10   8689
[2, 3, 6, 7, 8, 9, 10]
