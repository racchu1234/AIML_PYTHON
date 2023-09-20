import pandas as pd
data=[['racchu','female'],['sujatha','female'],['jairaj','male'],['keerthi','male']]
print(data)
print()
d1=pd.DataFrame(data,columns=["name","gender"])
print(d1)
print()
df1=pd.get_dummies(d1["gender"])
print(df1)
print()
df2=pd.concat((df1,d1),axis=1)
print(df2)
print()
df3=df2.drop(["gender"],axis=1)
print(df3)
print()
df4=df2.drop(["name"],axis=1)
print(df4)
result=df2.rename(columns={"female":"gender"})
print(result)
result1=df2.rename(columns={"gender":"female"})
print(result1)

output

[['racchu', 'female'], ['sujatha', 'female'], ['jairaj', 'male'], ['keerthi', 'male']]

      name  gender
0   racchu  female
1  sujatha  female
2   jairaj    male
3  keerthi    male

   female  male
0       1     0
1       1     0
2       0     1
3       0     1

   female  male     name  gender
0       1     0   racchu  female
1       1     0  sujatha  female
2       0     1   jairaj    male
3       0     1  keerthi    male

   female  male     name
0       1     0   racchu
1       1     0  sujatha
2       0     1   jairaj
3       0     1  keerthi

   female  male  gender
0       1     0  female
1       1     0  female
2       0     1    male
3       0     1    male
  gender  male     name  gender
0      1     0   racchu  female
1      1     0  sujatha  female
2      0     1   jairaj    male
3      0     1  keerthi    male
  female  male     name  female
0      1     0   racchu  female
1      1     0  sujatha  female
2      0     1   jairaj    male
3      0     1  keerthi    male
