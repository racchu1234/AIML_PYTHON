import numpy as np

arr2 = np.array(([[1, 2, 3], [4, 5, 6]]))
print(arr2)

print("sum of axis",arr2.sum(axis=1))
print("sum of array",arr2.sum())

print("avg of array",np.average(arr2))

print("min of array",arr2.min())
print("max of array",arr2.max())

print("min axis of array",arr2.min(axis=1))
print("max axis of array",arr2.max(axis=1))

print("sum",arr2.cumsum())
print("\ntransprote\n",arr2.T)


import numpy as np

arr = np.array([1, 12, 3, 4, 5])
print(arr)
arr1 = np.array([23, 4, 9, 10, 6])
print(arr1)
print("\nadd 2 array\n",arr+arr1)
print("\nsum 2 array\n",arr-arr1)
print("\nmulti 2 array\n",arr*arr1)
print("\ndivi 2 array\n",arr/arr1)
print("\nmod 2 array\n",arr%arr1)

output

[[1 2 3]
 [4 5 6]]
sum of axis [ 6 15]
sum of array 21
avg of array 3.5
min of array 1
max of array 6
min axis of array [1 4]
max axis of array [3 6]
sum [ 1  3  6 10 15 21]

transprote
 [[1 4]
 [2 5]
 [3 6]]
[ 1 12  3  4  5]
[23  4  9 10  6]

add 2 array
 [24 16 12 14 11]

sum 2 array
 [-22   8  -6  -6  -1]

multi 2 array
 [23 48 27 40 30]

divi 2 array
 [0.04347826 3.         0.33333333 0.4        0.83333333]

mod 2 array
 [1 0 3 4 5]
