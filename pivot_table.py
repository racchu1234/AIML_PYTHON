import pandas as pd
import numpy as np 

df=pd.DataFrame({"prodect":["banana","apple","chery"],"category":["f","v","v"],"quntity":[10,22,44],"amount":[100,200,400]})
table=df.pivot_table(index='amount',values='quntity',aggfunc='sum')

print(table) 

output

quntity
amount
100          10
200          22
400          44
