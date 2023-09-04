import pandas as pd
import numpy as np 

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/python/taitanic2.csv",index_col=('Survived'))
print(data)

print(data.shape)
print(data[['Age','Fare']])
print("\ngretar then 20\n",data.loc[data['Age']>20])
print("\n5 to 10\n",data.iloc[5:10])
print("\n2 to 10\n",data.iloc[2:5])


output

 PassengerId  Pclass  ... Cabin Embarked
Survived                       ...
0                   1       3  ...   NaN        S
1                   2       1  ...   C85        C
1                   3       3  ...   NaN        S
1                   4       1  ...  C123        S
0                   5       3  ...   NaN        S
              ...     ...  ...   ...      ...
0                 887       2  ...   NaN        S
1                 888       1  ...   B42        S
0                 889       3  ...   NaN        S
1                 890       1  ...  C148        C
0                 891       3  ...   NaN        Q

[891 rows x 11 columns]
(891, 11)
           Age     Fare
Survived
0         22.0   7.2500
1         38.0  71.2833
1         26.0   7.9250
1         35.0  53.1000
0         35.0   8.0500
       ...      ...
0         27.0  13.0000
1         19.0  30.0000
0          NaN  23.4500
1         26.0  30.0000
0         32.0   7.7500

[891 rows x 2 columns]

gretar then 20
           PassengerId  Pclass  ... Cabin Embarked
Survived                       ...
0                   1       3  ...   NaN        S
1                   2       1  ...   C85        C
1                   3       3  ...   NaN        S
1                   4       1  ...  C123        S
0                   5       3  ...   NaN        S
              ...     ...  ...   ...      ...
0                 885       3  ...   NaN        S
0                 886       3  ...   NaN        Q
0                 887       2  ...   NaN        S
1                 890       1  ...  C148        C
0                 891       3  ...   NaN        Q

[535 rows x 11 columns]

5 to 10
           PassengerId  Pclass  ... Cabin Embarked
Survived                       ...
0                   6       3  ...   NaN        Q

