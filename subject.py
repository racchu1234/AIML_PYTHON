import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns

maths=[23,56,89,78,34,56]
science=[56,34,78,23,54,12]
social=[45,78,90,34,56,78]
df=pd.DataFrame({'mathas':maths,'science':science,'social':social})
print(df)
print(df.plot.bar())
print(df.plot.density())
print(df.boxplot())

output

mathas  science  social
0      23       56      45
1      56       34      78
2      89       78      90
3      78       23      34
4      34       54      56
5      56       12      78
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
