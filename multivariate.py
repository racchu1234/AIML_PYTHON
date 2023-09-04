import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/titanic.csv")
print(data)
print(sns.catplot(x='Embarked',hue='Survived',col='Sex',data=data,kind='count'))
print(sns.catplot(x='Pclass',hue='Sex',col='Survived',data=data,kind='count'))

output

PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0              1         0       3  ...   7.2500   NaN         S
1              2         1       1  ...  71.2833   C85         C
2              3         1       3  ...   7.9250   NaN         S
3              4         1       1  ...  53.1000  C123         S
4              5         0       3  ...   8.0500   NaN         S
..           ...       ...     ...  ...      ...   ...       ...
886          887         0       2  ...  13.0000   NaN         S
887          888         1       1  ...  30.0000   B42         S
888          889         0       3  ...  23.4500   NaN         S
889          890         1       1  ...  30.0000  C148         C
890          891         0       3  ...   7.7500   NaN         Q

[891 rows x 12 columns]
<seaborn.axisgrid.FacetGrid object at 0x000001BD0BBD4FD0>
<seaborn.axisgrid.FacetGrid object at 0x000001BD0BBD4520>
