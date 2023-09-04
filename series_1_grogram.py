import pandas as pd
import numpy as np 

data={"racchu": [18],"acchu":[18],"paru":[18],"nagu":[18]}
df = pd.DataFrame(data)
print(df)

print()

data1={"name":['acchu','paru','nagu'],"age":[18,18,18]}
df1 = pd.DataFrame(data1)
print(df1)

output

racchu  acchu  paru  nagu
0      18     18    18    18

    name  age
0  acchu   18
1   paru   18
2   nagu   18
