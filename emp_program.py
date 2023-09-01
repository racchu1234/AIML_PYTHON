import pandas as pd
import numpy as np 

#q1 read data
data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/emp dataset.csv")
print(data)

print(data[data['Gender']=='Male']['Dept']=='HR')
print(data[data['Gender']=='Female']['Dept']=='Technology')

print(data.groupby('Dept')['salary'].sum())

output

   Unnamed: 0    emp_id  age        Dept  ... salary satisfied  Gender     name
0             0    HR8270   28          HR  ...  86750         1  Female   racchu
1             1  TECH1860   50  Technology  ...  42419         0    Male    acchu
2             2  TECH6390   43  Technology  ...  65715         0    Male     paru
3             3   SAL6191   44       Sales  ...  29805         1  Female     nagu
4             4    HR6734   33          HR  ...  29805         1    Male  sujatha
..          ...       ...  ...         ...  ...    ...       ...     ...      ...
495         495    HR5330   49          HR  ...  29805         1     NaN      NaN
496         496  TECH9010   24  Technology  ...  29805         0     NaN      NaN
497         497   MKT7801   34   Marketing  ...  24076         1     NaN      NaN
498         498  TECH5846   26  Technology  ...  29805         0     NaN      NaN
499         499  TECH7731   26  Technology  ...  42419         0     NaN      NaN

[500 rows x 16 columns]
1      False
2      False
4       True
5      False
6      False

407    False
408    False
409     True
410    False
411    False
Name: Dept, Length: 262, dtype: bool
0      False
3      False
8      False
9       True
13     False

399    False
400     True
402    False
404    False
406     True
Name: Dept, Length: 150, dtype: bool
Dept
HR            5260755
Marketing     4761653
Purchasing    5946576
Sales         4921363
Technology    4317681
Name: salary, dtype: int64
