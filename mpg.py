import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

#q1 read data
data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/auto-mpg.csv")
print(data)
print(data.head(10))
plt.hist(x=data['mpg'])

plt.scatter(x='weight',y='mpg',data=data)
print(data['origin'].value_counts().plot(kind='bar'))
print(sns.boxplot(data['mpg']))
print(data['mpg'].min())


output

 mpg  cylinders  ...  origin                   car name
0    18.0          8  ...       1  chevrolet chevelle malibu
1    15.0          8  ...       1          buick skylark 320
2    18.0          8  ...       1         plymouth satellite
3    16.0          8  ...       1              amc rebel sst
4    17.0          8  ...       1                ford torino
..    ...        ...  ...     ...                        ...
393  27.0          4  ...       1            ford mustang gl
394  44.0          4  ...       2                  vw pickup
395  32.0          4  ...       1              dodge rampage
396  28.0          4  ...       1                ford ranger
397  31.0          4  ...       1                 chevy s-10

[398 rows x 9 columns]
    mpg  cylinders  displacement  ... model year  origin                   car name
0  18.0          8         307.0  ...       70.0       1  chevrolet chevelle malibu
1  15.0          8         350.0  ...       70.0       1          buick skylark 320
2  18.0          8         318.0  ...       70.0       1         plymouth satellite
3  16.0          8         304.0  ...       70.0       1              amc rebel sst
4  17.0          8         302.0  ...       70.0       1                ford torino
5  15.0          8         429.0  ...       70.0       1           ford galaxie 500
6  14.0          8         454.0  ...       70.0       1           chevrolet impala
7  14.0         50         440.0  ...       70.0       1          plymouth fury iii
8  14.0          8         455.0  ...       70.0       1           pontiac catalina
9  15.0          8         390.0  ...        NaN       1         amc ambassador dpl

[10 rows x 9 columns]
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
9.0
