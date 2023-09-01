import pandas as pd
import numpy as np 


data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/emp dataset1.csv")
print(pd.DataFrame(data))
table=data.pivot_table(index=['type','Dept'],values='salary',aggfunc='mean')
print(table) 
table=data.pivot_table(index='type',values='salary',aggfunc=['mean','sum','count'])
print(table) 

output

     Unnamed: 0    emp_id  age  ...  Gender     name       type
0             0    HR8270   28  ...  Female   racchu   full tme
1             1  TECH1860   50  ...    Male    acchu     intern
2             2  TECH6390   43  ...    Male     paru  full time
3             3   SAL6191   44  ...  Female     nagu  part time
4             4    HR6734   33  ...    Male  sujatha  full time
..          ...       ...  ...  ...     ...      ...        ...
495         495    HR5330   49  ...     NaN      NaN        NaN
496         496  TECH9010   24  ...     NaN      NaN        NaN
497         497   MKT7801   34  ...     NaN      NaN        NaN
498         498  TECH5846   26  ...     NaN      NaN        NaN
499         499  TECH7731   26  ...     NaN      NaN        NaN

[500 rows x 17 columns]
                        salary
type      Dept
full time HR          29805.00
          Marketing   24076.00
          Purchasing  86750.00
          Sales       86750.00
          Technology  40503.75
full tme  HR          86750.00
intern    Purchasing  70408.50
          Technology  42419.00
part time HR          33247.50
          Marketing   65715.00
          Purchasing  42419.00
          Sales       29805.00
                   mean     sum  count
                 salary  salary salary
type
full time  48674.500000  389396      8
full tme   86750.000000   86750      1
intern     61078.666667  366472      6
part time  40886.800000  204434      5
