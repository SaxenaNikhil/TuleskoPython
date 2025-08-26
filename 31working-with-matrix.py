from numpy import *
# If you have multiple arrays inside of an array then it's an multidimensional array.

arr1 = array([
    [1, 2, 3],
    [4, 5, 6]
])

print('Printing a multi-dimensional array - ',arr1)
# To check the type of data you are working with then use the dtype
print('Data type of an array - ',arr1.dtype)

# To check the dimension use 'ndim'
print('Dimension of an array - ',arr1.ndim)
# For single dimension value it will give 1, for 2 dimension value it will give 2 and for 3 dimension value it will give 3.

# Array shape gives you the number of rows and columns, so we have 2 rows and 3 columns so it will give you tuple with number of rows and number of columns
print('Array Shape - ',arr1.shape)

# Array Size -  It will tell the size of the entire block you can count it now which is 3 and 3 i.e. 6
print('Array Size - ', arr1.size)

# Convert a 2D array to 1D array using the function 'flatten'
arr2 = arr1.flatten()
print('1D Array - ', arr2)

# Converting single dimension 1D to multidimensional
arr11 = array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

arr22 = arr11.flatten()
print('Multidimensional to 1D array - ',arr22)

# Now creating a one dimensional array to 3 dimensional array. So you can use this reshape() function to pass the rows and columns. reshape(3, 4) is 3 rows and 4 columns.

arr33 = arr22.reshape(3, 4)
print('1D to 2D array - ', arr33)
print('Dimension of array - ',arr33.ndim)
# Here since we have passed only 2 values in reshape function i.e. rows and columns then this array is a 2D array and not 3D array as we can check it using the ndim() function as well.

# Now to create a 3D array from a 1D array -
arr44 = arr22.reshape(2, 2, 3)
# Here in the reshape(2, 2, 3) function looks like this in the output -
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]]

# This means that First dimension = 2 → This means the array has 2 blocks.
# Second dimension = 2 → Each block has 2 rows.
# Third dimension = 3 → Each row has 3 columns (or elements).
# So inside a first array as 2 array block and inside 1st array block it has 2 rows [0 1 2] [3 4 5] and each row has 3 columns

print('1D to 3D array - ',arr44)
print('Dimension of array - ',arr44.ndim)

print('# >>>>>>>>>>>>>>>>>')
# Matrix
# Matrices - 2D array which have multiple rows and multiple columns
# Row matrices has 1 row but multiple columns such as - [1, 2, 3, 4, 5, 6] therefore it still be 1D array.
# Column matrices has 1 column but multiple rows which is like a standing array. therefore it still be 1D array.
# Matrix format has multiple rows multiple columns

# Converting 2D array into matrix format using the matrix() function.

arr55 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

print('2D array before matrix - ', arr55)

m = matrix(arr55)
print('printing matrix - ',m)
# Although the output is same as the array when printed but the difference is that with this 'm' we can perform more operations in matrices.

# Matrices can also work even if we don't have 2D array and if we have a string or input from a user.
m = matrix('1 2 3 4 ; 5 6 7 8')
print('2D matrix - ',m)

# If you want to create 4 rows and 2 columns m = matrix('1 2 ; 3 4 ; 5 6 ; 7 8')
m = matrix('1 2 ; 3 4 ; 5 6 ; 7 8')
print('4 rows 2 columns matrix - ', m)

# Minimum elements
print('Minimum elements - ', m.min())

# Maximum elements
print('Maximum elements - ', m.max())

# Multiply two matrices
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('9 8 7; 6 5 4; 3 2 1')

m3 = m1 + m2

print('Adding two matrices - ', m3)

m4 = m1 * m2
print('Multiply two matrices - ', m4)