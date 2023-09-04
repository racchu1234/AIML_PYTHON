import pandas as pd
import numpy as np 

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/python/taitanic2.csv",index_col=('Cabin'))[:150]
print(data)
data1=pd.DataFrame(data)
print(data1)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-100))
print(data.dropna())
print(data.dropna(how="all"))

output


PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass   Name  ...  Parch  Ticket   Fare  Embarked
Cabin                                        ...
NaN          False     False   False  False  ...  False   False  False     False
C85          False     False   False  False  ...  False   False  False     False
NaN          False     False   False  False  ...  False   False  False     False
C123         False     False   False  False  ...  False   False  False     False
NaN          False     False   False  False  ...  False   False  False     False
           ...       ...     ...    ...  ...    ...     ...    ...       ...
NaN          False     False   False  False  ...  False   False  False     False
NaN          False     False   False  False  ...  False   False  False     False
NaN          False     False   False  False  ...  False   False  False     False
F2           False     False   False  False  ...  False   False  False     False
NaN          False     False   False  False  ...  False   False  False     False

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  Name  ...  Parch  Ticket  Fare  Embarked
Cabin                                       ...
NaN           True      True    True  True  ...   True    True  True      True
C85           True      True    True  True  ...   True    True  True      True
NaN           True      True    True  True  ...   True    True  True      True
C123          True      True    True  True  ...   True    True  True      True
NaN           True      True    True  True  ...   True    True  True      True
           ...       ...     ...   ...  ...    ...     ...   ...       ...
NaN           True      True    True  True  ...   True    True  True      True
NaN           True      True    True  True  ...   True    True  True      True
NaN           True      True    True  True  ...   True    True  True      True
F2            True      True    True  True  ...   True    True  True      True
NaN           True      True    True  True  ...   True    True  True      True

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[120 rows x 11 columns]
       PassengerId  Survived  Pclass  ...            Ticket     Fare  Embarked
Cabin                                 ...
NaN              1         0       3  ...         A/5 21171   7.2500         S
C85              2         1       1  ...          PC 17599  71.2833         C
NaN              3         1       3  ...  STON/O2. 3101282   7.9250         S
C123             4         1       1  ...            113803  53.1000         S
NaN              5         0       3  ...            373450   8.0500         S
           ...       ...     ...  ...               ...      ...       ...
NaN            146         0       2  ...        C.A. 33112  36.7500         S
NaN            147         1       3  ...            350043   7.7958         S
NaN            148         0       3  ...        W./C. 6608  34.3750         S
F2             149         0       2  ...            230080  26.0000         S
NaN            150         0       2  ...            244310  13.0000         S

[150 rows x 11 columns]
