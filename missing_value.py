import pandas as pd
import seaborn as sns
data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/titanic.csv") 
print(data)
print(data.info())
print(data.isna().sum())
sns.heatmap(data.isna())
print(data.shape)
print(data.dropna(inplace=True))
print(data.shape)
data1 = data.drop(['Cabin'],axis=1)
print(data1)
print(data.shape)
sns.heatmap(data.isna())
print('\n missing value\n',data.isna().sum())
print(data.info())

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
<class 'pandas.core.frame.DataFrame'>
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
(891, 12)
None
(183, 12)
     PassengerId  Survived  Pclass  ...    Ticket     Fare  Embarked
1              2         1       1  ...  PC 17599  71.2833         C
3              4         1       1  ...    113803  53.1000         S
6              7         0       1  ...     17463  51.8625         S
10            11         1       3  ...   PP 9549  16.7000         S
11            12         1       1  ...    113783  26.5500         S
..           ...       ...     ...  ...       ...      ...       ...
871          872         1       1  ...     11751  52.5542         S
872          873         0       1  ...       695   5.0000         S
879          880         1       1  ...     11767  83.1583         C
887          888         1       1  ...    112053  30.0000         S
889          890         1       1  ...    111369  30.0000         C

[183 rows x 11 columns]
(183, 12)

 missing value
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
Cabin          0
Embarked       0
dtype: int64
<class 'pandas.core.frame.DataFrame'>
Int64Index: 183 entries, 1 to 889
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  183 non-null    int64
 1   Survived     183 non-null    int64
 2   Pclass       183 non-null    int64
 3   Name         183 non-null    object
 4   Sex          183 non-null    object
 5   Age          183 non-null    float64
 6   SibSp        183 non-null    int64
 7   Parch        183 non-null    int64
 8   Ticket       183 non-null    object
 9   Fare         183 non-null    float64
 10  Cabin        183 non-null    object
 11  Embarked     183 non-null    object
dtypes: float64(2), int64(5), object(5)
memory usage: 18.6+ KB
None
