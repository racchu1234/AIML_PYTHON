import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns

dummy_age=[18,90,60,80,67,45]
dummy_sex=['female','male','male','female','feamle','male']
df=pd.DataFrame({'age':dummy_age,"sex":dummy_sex})
print(df)
print(df['age'].hist())
sns.set(style='darkgrid')
a=sns.countplot(x='sex',data=df)

output

 age     sex
0   18  female
1   90    male
2   60    male
3   80  female
4   67  feamle
5   45    male
AxesSubplot(0.125,0.125;0.775x0.755)
