import pandas as pd
import numpy as np 

df=pd.DataFrame({"tumkur":[10,20,45],"chitradurga":[25,30,59],"banglore":[78,90,76]})

print(df)
print(df.melt())

output

tumkur  chitradurga  banglore
0      10           25        78
1      20           30        90
2      45           59        76
      variable  value
0       tumkur     10
1       tumkur     20
2       tumkur     45
3  chitradurga     25
4  chitradurga     30
5  chitradurga     59
6     banglore     78
7     banglore     90
8     banglore     76
