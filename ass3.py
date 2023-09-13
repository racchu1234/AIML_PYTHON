import pandas as pd
import numpy as np 
import matplotlib.pyplot as pl
import seaborn as sns

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/mtcars.csv")
print(data)
print(data.head(5))
print(data.info())
print(data.shape)
print(data.describe())
print(data['mpg'].hist())
sns.countplot(x='am',data=data)
print(data['am'].value_counts())

print(data['mpg'].value_counts().plot(kind='bar'))
print(data['mpg'].plot.density())
print(sns.boxplot(x='mpg',data=data))
print(sns.scatterplot(x=data['wt'],y=data['mpg']))
sns.countplot(x='am',hue='cyl',data=data)
print(sns.catplot(x='carb',hue='gear',col='vs',data=data,kind='count'))
print(sns.catplot(x='am',hue='carb',col='vs',data=data,kind='count'))

output

model   mpg  cyl   disp   hp  ...  vs  am  gear  carb  modal_year
0             Mazda RX4  21.0    6  160.0  110  ...   0   1     4     4          70
1         Mazda RX4 Wag  21.0    6  160.0  110  ...   0   1     4     4          60
2            Datsun 710  22.8    4  108.0   93  ...   1   1     4     1          65
3        Hornet 4 Drive  21.4    6  258.0  110  ...   1   0     3     1          45
4     Hornet Sportabout  18.7    8  360.0  175  ...   0   0     3     2          85
5               Valiant  18.1    6  225.0  105  ...   1   0     3     1          62
6            Duster 360  14.3    8  360.0  245  ...   0   0     3     4          45
7             Merc 240D  24.4    4  146.7   62  ...   1   0     4     2          85
8              Merc 230  22.8    4  140.8   95  ...   1   0     4     2          36
9              Merc 280  19.2    6  167.6  123  ...   1   0     4     4          88
10            Merc 280C  17.8    6  167.6  123  ...   1   0     4     4          71
11           Merc 450SE  16.4    8  275.8  180  ...   0   0     3     3          64
12           Merc 450SL  17.3    8  275.8  180  ...   0   0     3     3          64
13          Merc 450SLC  15.2    8  275.8  180  ...   0   0     3     3          70
14   Cadillac Fleetwood  10.4    8  472.0  205  ...   0   0     3     4          65
15  Lincoln Continental  10.4    8  460.0  215  ...   0   0     3     4          75
16    Chrysler Imperial  14.7    8  440.0  230  ...   0   0     3     4          80
17             Fiat 128  32.4    4   78.7   66  ...   1   1     4     1          85
18          Honda Civic  30.4    4   75.7   52  ...   1   1     4     2          84
19       Toyota Corolla  33.9    4   71.1   65  ...   1   1     4     1          63
20        Toyota Corona  21.5    4  120.1   97  ...   1   0     3     1          52
21     Dodge Challenger  15.5    8  318.0  150  ...   0   0     3     2          44
22          AMC Javelin  15.2    8  304.0  150  ...   0   0     3     2          56
23           Camaro Z28  13.3    8  350.0  245  ...   0   0     3     4          57
24     Pontiac Firebird  19.2    8  400.0  175  ...   0   0     3     2          74
25            Fiat X1-9  27.3    4   79.0   66  ...   1   1     4     1          60
26        Porsche 914-2  26.0    4  120.3   91  ...   0   1     5     2          68
27         Lotus Europa  30.4    4   95.1  113  ...   1   1     5     2          69
28       Ford Pantera L  15.8    8  351.0  264  ...   0   1     5     4          73
29         Ferrari Dino  19.7    6  145.0  175  ...   0   1     5     6          72
30        Maserati Bora  15.0    8  301.0  335  ...   0   1     5     8          84
31           Volvo 142E  21.4    4  121.0  109  ...   1   1     4     2          54

[32 rows x 13 columns]
               model   mpg  cyl   disp   hp  ...  vs  am  gear  carb  modal_year
0          Mazda RX4  21.0    6  160.0  110  ...   0   1     4     4          70
1      Mazda RX4 Wag  21.0    6  160.0  110  ...   0   1     4     4          60
2         Datsun 710  22.8    4  108.0   93  ...   1   1     4     1          65
3     Hornet 4 Drive  21.4    6  258.0  110  ...   1   0     3     1          45
4  Hornet Sportabout  18.7    8  360.0  175  ...   0   0     3     2          85

[5 rows x 13 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32 entries, 0 to 31
Data columns (total 13 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   model       32 non-null     object
 1   mpg         32 non-null     float64
 2   cyl         32 non-null     int64
 3   disp        32 non-null     float64
 4   hp          32 non-null     int64
 5   drat        32 non-null     float64
 6   wt          32 non-null     float64
 7   qsec        32 non-null     float64
 8   vs          32 non-null     int64
 9   am          32 non-null     int64
 10  gear        32 non-null     int64
 11  carb        32 non-null     int64
 12  modal_year  32 non-null     int64
dtypes: float64(5), int64(7), object(1)
memory usage: 3.4+ KB
None
(32, 13)
             mpg        cyl        disp  ...       gear     carb  modal_year
count  32.000000  32.000000   32.000000  ...  32.000000  32.0000   32.000000
mean   20.090625   6.187500  230.721875  ...   3.687500   2.8125   66.406250
std     6.026948   1.785922  123.938694  ...   0.737804   1.6152   13.440093
min    10.400000   4.000000   71.100000  ...   3.000000   1.0000   36.000000
25%    15.425000   4.000000  120.825000  ...   3.000000   2.0000   59.250000
50%    19.200000   6.000000  196.300000  ...   4.000000   2.0000   66.500000
75%    22.800000   8.000000  326.000000  ...   4.000000   4.0000   74.250000
max    33.900000   8.000000  472.000000  ...   5.000000   8.0000   88.000000

[8 rows x 12 columns]
AxesSubplot(0.125,0.125;0.775x0.755)
0    19
1    13
Name: am, dtype: int64
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
AxesSubplot(0.125,0.125;0.775x0.755)
<seaborn.axisgrid.FacetGrid object at 0x000002317A52CCD0>
<seaborn.axisgrid.FacetGrid object at 0x000002317A51BE20>
