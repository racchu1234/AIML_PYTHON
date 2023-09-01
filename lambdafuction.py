#lambda
print()
print("....lambda....")
print()

a=lambda x:x+5
print(a(2))

b=lambda x,y:x+y
print(b(6,9))

c=lambda x,y:x if (x>y) else y
print(c(34,90))

d=lambda x,y:x if (x<y) else y
print(d(34,90))

e=lambda x:x*x
print(e(3))

#map
print()
print("...map...")
print()

lst=[1,2,3,4,5]
l=list(map(lambda x:x+5,lst))
print(l)

#filter
print()
print("...filter...")
print()

lst=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(lambda x:x%2,lst))
print("even numbers",l1)

lst=[1,2,3,4,5,6,7,8,9,10]
l2=list(filter(lambda x:x%2==0,lst))
print("odd number",l2)

#reduce
print()
print("...reduce....")
print()

from functools import reduce
lst=[1,2,3,4,5,6,7,8,9,10]
l2=reduce(lambda x,y:x+y,lst)
print(l2)

lst1=[1,2,3,4,5,6,7,8,9,10,90]
l3=reduce(lambda x,y: x if (x>y) else y,lst1)
print(l3)

lst2=[100,2,3,4,5,6,7,8,9,10,90,89]
l4=reduce(lambda x,y: x if (x<y) else y,lst2)
print(l4)

lst=[1,2,3,4,5,6,7,8,9,100]
l5=reduce(lambda x,y:x-y,lst)
print(l5)

lst=[1,2,3,4,5,6,7,8,9,10]
l6=reduce(lambda x,y:x*y,lst)
print(l6)

lst=[1,2,3,4,5,6,7,8,9,10]
l7=reduce(lambda x,y:x%y,lst)
print(l7)



output


....lambda....

7
15
90
34
9

...map...

[6, 7, 8, 9, 10]

...filter...

even numbers [1, 3, 5, 7, 9]
odd number [2, 4, 6, 8, 10]

...reduce....

55
90
2
-143
3628800
1
