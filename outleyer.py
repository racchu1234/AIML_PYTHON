import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/titanic.csv")
print(data.info())
print(data.isnull().sum())
sns.heatmap(data.isna())
data = data.drop(['Cabin'],axis=1)
print(data.isnull().sum())
print(data.shape)
m = data['Age'].mean()
print('mean',m)
data['Age'].fillna(m,inplace=True)
print(data.isnull().sum())
mode = data['Embarked'].mode()
print(mode)
data['Embarked']=data['Embarked'].fillna(data['Embarked'].mode()[0])
print(data.isnull().sum())
sns.boxplot(data['Age'])
plt.show()
med=data['Age'].median()
print("median ",med)
data['Age'].fillna(med,inplace=True)
Q1 = data['Age'].quantile(0.25)
print(Q1)
Q3 = data['Age'].quantile(0.75)
print(Q3)
IQR = Q3-Q1
lw = Q1-(1.5*IQR)
uw = Q3+(1.5*IQR)
data['Age'] = np.where(data['Age'] > uw, uw, np.where(data['Age'] < lw, lw, data['Age']))
sns.boxplot(data['Age'])
plt.show()
ind=(data['Age']>uw)|(data['Age']<lw)
index1=data[ind].index
print(index1)
print(data.drop(index1,inplace=True))
print(data.shape)
sns.boxplot(data['Age'])

output

RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  891 non-null    int64
 1   Survived     891 non-null    int64
 2   Pclass       891 non-null    int64
 3   Name         891 non-null    object
 4   Sex          891 non-null    object
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64
 7   Parch        891 non-null    int64
 8   Ticket       891 non-null    object
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object
 11  Embarked     889 non-null    object
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
None
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Embarked         2
dtype: int64
(891, 11)
mean 29.69911764705882
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            0
SibSp          0
Parch          0
Ticket         0
Fare           0
Embarked       2
dtype: int64
0    S
Name: Embarked, dtype: object
PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            0
SibSp          0
Parch          0
Ticket         0
Fare           0
Embarked       0
dtype: int64
