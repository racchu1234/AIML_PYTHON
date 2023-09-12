import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/bankloan.csv")
print(data)
dat=data.drop(['Loan ID'],axis=1)
x=data.iloc[:,-1].values.reshape(-1,1)
print(x)
y=data['loan amount'].values.reshape(-1,1)
print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=(0.2),random_state=4)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


from sklearn.linear_model import LinearRegression

lm=LinearRegression()
lm.fit(x_train,y_train)
ypredict=lm.predict(x_test)
print(ypredict)

output

                                   Loan ID  ...  loan amount
0     f738779f-c726-40dc-92cf-689d73af533d  ...      1058970
1     6dcc0947-164d-476c-a1de-3ae7283dde0a  ...       904442
2     f7744d01-894b-49c3-8777-fc6431a2cff1  ...       388036
3     83721ffb-b99a-4a0f-aea5-ef472a138b41  ...       531322
4     08f3789f-5714-4b10-929d-e1527ab5e5a3  ...       468072
                                   ...  ...          ...
9995  c4ab66f9-833c-43b8-879c-4f8bcb64dd14  ...       234410
9996  bbd3a392-01b4-4e0e-9c28-b2a4a39beac7  ...       329692
9997  da9870de-4280-46a3-8fc6-91cfe5bfde9d  ...       568370
9998  0cc8e0e0-1bc6-49d7-ad0f-0598b647458f  ...       240658
9999  14f94b64-26c4-48fd-b916-1388d7adcc1d  ...       607882

[10000 rows x 6 columns]
[[1058970]
 [ 904442]
 [ 388036]
 ...
 [ 568370]
 [ 240658]
 [ 607882]]
[[1058970]
 [ 904442]
 [ 388036]
 ...
 [ 568370]
 [ 240658]
 [ 607882]]
[[ 199782]
 [ 272184]
 [1862564]
 ...
 [  51546]
 [ 472230]
 [ 347116]]
[[826232]
 [263208]
 [337546]
 ...
 [793562]
 [805574]
 [358644]]
[[ 199782]
 [ 272184]
 [1862564]
 ...
 [  51546]
 [ 472230]
 [ 347116]]
[[826232]
 [263208]
 [337546]
 ...
 [793562]
 [805574]
 [358644]]
[[826232.]
 [263208.]
 [337546.]
 ...
 [793562.]
 [805574.]
 [358644.]]

