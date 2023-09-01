import pandas as pd
import numpy as np 


s1=pd.Series([1,4,5,4,6,7])
s2=pd.Series([4,6,7,8,10])
u=pd.Series(np.union1d(s1,s2))
print("\n.........union........ \n",u)
i=pd.Series(np.intersect1d(s1,s2))
print("\n.......intersect.......\n",i)
nc=u[~u.isin (i)]
print("\ndelete comman numbers\n",nc)

output
.........union........
 0     1
1     4
2     5
3     6
4     7
5     8
6    10
dtype: int64

.......intersect.......
 0    4
1    6
2    7
dtype: int64

delete comman numbers
 0     1
2     5
5     8
6    10
dtype: int64
