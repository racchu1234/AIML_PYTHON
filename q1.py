import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/titanic123.csv")
print(data)
print(data.head(10))
plt.hist(data['Age'])
print(data['Age'].max())
info=data['Sex'=='female']
print(data[data['Pclass']==3]['Survived'].value_counts().plot(kind='bar'))
print(plt.scatter(x=data['Age'],y=data['Fare']))


