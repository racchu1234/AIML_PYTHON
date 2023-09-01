import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/iris.csv")
print(data)
plt.scatter(data['sepal_length'],data['petal_length'])
plt.title("scatter plot")
plt.xlabel('sepal_length')
plt.ylabel('petal_length')
plt.show()

plt.plot(data['sepal_width'])
plt.plot(data['petal_width'])
plt.title("line chart")
plt.xlabel('sepal_width')
plt.ylabel('petal_width')
plt.show()

plt.bar(data['sepal_length'],data['sepal_width'])
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.title("bar plot")
plt.show()

plt.hist(data['sepal_width'])
print(data['sepal_length'].max())
print(data['sepal_length'].value_counts())
plt.title("histogram")

print(data['petal_width'].hist())
sns.set(style='darkgrid')
a=sns.countplot(x='petal_length',data=data)


output

   sepal_length  sepal_width  petal_length  petal_width    species
0             5.1          3.5           1.4          0.2     setosa
1             4.9          3.0           1.4          0.2     setosa
2             4.7          3.2           1.3          0.2     setosa
3             4.6          3.1           1.5          0.2     setosa
4             5.0          3.6           1.4          0.2     setosa
..            ...          ...           ...          ...        ...
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica

[150 rows x 5 columns]
7.9
5.0    10
5.1     9
6.3     9
5.7     8
6.7     8
5.8     7
5.5     7
6.4     7
4.9     6
5.4     6
6.1     6
6.0     6
5.6     6
4.8     5
6.5     5
6.2     4
7.7     4
6.9     4
4.6     4
5.2     4
5.9     3
4.4     3
7.2     3
6.8     3
6.6     2
4.7     2
7.6     1
7.4     1
7.3     1
7.0     1
7.1     1
5.3     1
4.3     1
4.5     1
7.9     1
Name: sepal_length, dtype: int64
AxesSubplot(0.125,0.125;0.775x0.755)
