import pandas as pd
import numpy as np 

data={'days':[1,2,3,4,5,6,7,8,9,10],'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
data1=pd.DataFrame(data)
print(data1)

print(data1.loc[data1['steps']>7000])

output

days  steps
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
   days  steps
1     2   9552
2     3   7332
5     6   7552
6     7   8332
8     9   8965
9    10   7689
