a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
l1=list(map(lambda a, b, c:a+b+c,a,b,c ))
print(l1)

lst=["mango","apple","orange","banana"]
l2=list(filter(lambda x:"g" in x ,lst))
print(l2)

lst1=["cat","dog","book","pen","goat","good"]
l3=list(filter(lambda x:"o" in x ,lst1))
print(l3)

lst2=["cat","dog","book","pen","goat","good"]
l4=list(filter(lambda x:"g" in x ,lst2))
print(l4)

output

[12, 15, 18]
['mango', 'orange']
['dog', 'book', 'goat', 'good']
['dog', 'goat', 'good']
