import numpy as np
arr = np.array([2, 5, 6, 5, 6,8,2,9,6])
print(arr)
print("Shape of the matrix is = ",arr.shape)
re = arr.reshape(3,3)
print("Reshape the Matrix into 3,3, is =\n",re)
mal = re*2
print("Multiplay by 2 is = \n",mal)

add = re+2
print("Add 2 with matrix is = \n",add)

sub = re-2
print("Subraction of matrix by 2 is  = \n",sub)

div = re/2
print("Divided with matrix by 2 is = \n",div)

output

[2 5 6 5 6 8 2 9 6]
Shape of the matrix is =  (9,)
Reshape the Matrix into 3,3, is =
 [[2 5 6]
 [5 6 8]
 [2 9 6]]
Multiplay by 2 is =
 [[ 4 10 12]
 [10 12 16]
 [ 4 18 12]]
Add 2 with matrix is =
 [[ 4  7  8]
 [ 7  8 10]
 [ 4 11  8]]
Subraction of matrix by 2 is  =
 [[0 3 4]
 [3 4 6]
 [0 7 4]]
Divided with matrix by 2 is =
 [[1.  2.5 3. ]
 [2.5 3.  4. ]
 [1.  4.5 3. ]]
