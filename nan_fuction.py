import pandas as pd
import numpy as np
dict={ 'first score':[np.nan,30,np.nan,60],
       'second score':[np.nan,40,50,30],
       'third score':[np.nan,30,np.nan,50]}
data=pd.DataFrame(dict)
print(data)

print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-99))
print(data.dropna())
print(data.dropna(how="all"))

output

first score  second score  third score
0          NaN           NaN          NaN
1         30.0          40.0         30.0
2          NaN          50.0          NaN
3         60.0          30.0         50.0
   first score  second score  third score
0         True          True         True
1        False         False        False
2         True         False         True
3        False         False        False
   first score  second score  third score
0        False         False        False
1         True          True         True
2        False          True        False
3         True          True         True
   first score  second score  third score
0          0.0           0.0          0.0
1         30.0          40.0         30.0
2          0.0          50.0          0.0
3         60.0          30.0         50.0
   first score  second score  third score
0          NaN           NaN          NaN
1         30.0          40.0         30.0
2         30.0          50.0         30.0
3         60.0          30.0         50.0
   first score  second score  third score
0         30.0          40.0         30.0
1         30.0          40.0         30.0
2         60.0          50.0         50.0
3         60.0          30.0         50.0
   first score  second score  third score
0        -99.0         -99.0        -99.0
1         30.0          40.0         30.0
2        -99.0          50.0        -99.0
3         60.0          30.0         50.0
   first score  second score  third score
1         30.0          40.0         30.0
3         60.0          30.0         50.0
   first score  second score  third score
1         30.0          40.0         30.0
2          NaN          50.0          NaN
3         60.0          30.0         50.0
