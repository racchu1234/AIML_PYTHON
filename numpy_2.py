import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#creating 2D array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#Reshaping 1D to 2D
import numpy as np
arr = np.array([[1, 2,10],[19,3,12]])
newarr = arr.reshape(3,2)
print(newarr)
print("no of dimensions:",arr.ndim)
print("array is of type:",arr.dtype)
print("size os array",arr.size)

import numpy as np
arr=np.array([[1,2,3],[4,5,6]],dtype='float')
print("\narry created using passed list:\n",arr)

arr2=np.array((4,6,7))
print("\n narry created using passed tuple",arr2)

arr3=np.zeros((3,4))
print(arr3)

arr=np.full((2,5),6,dtype='float')
print("\narry created using passed list:\n",arr)

output

[1 2 3 4 5]
[[1 2 3]
 [4 5 6]]
[[ 1  2]
 [10 19]
 [ 3 12]]
no of dimensions: 2
array is of type: int32
size os array 6

arry created using passed list:
 [[1. 2. 3.]
 [4. 5. 6.]]

 narry created using passed tuple [4 6 7]
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

arry created using passed list:
 [[6. 6. 6. 6. 6.]
 [6. 6. 6. 6. 6.]]
