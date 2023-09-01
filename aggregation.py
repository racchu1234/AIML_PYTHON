import pandas as pd
import numpy as np 

data=pd.DataFrame([[10,11,12,13],[10,11,12,13]],columns=["maths","seicence","kannada","english"])
print(data)

print("\nsum of subjects\n",data.sum())
print(data['maths'].sum())
print(data['seicence'].min())
print(data['kannada'].max())
print(data['english'].max())
print(data.value_counts())
print(data['kannada'].value_counts())
print(data.agg(['sum','max']))

output

maths  seicence  kannada  english
0     10        11       12       13
1     10        11       12       13

sum of subjects
 maths       20
seicence    22
kannada     24
english     26
dtype: int64
20
11
12
13
maths  seicence  kannada  english
10     11        12       13         2
dtype: int64
12    2
Name: kannada, dtype: int64
     maths  seicence  kannada  english
sum     20        22       24       26
max     10        11       12       13

