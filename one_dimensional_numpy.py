# Import numpy library
import numpy as np

# Create a numpy array

a = np.array([0,1,2,3,4])
a

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# The version string is stored under version attribute
print(np.__version__)

# Check the type of the array

type(a)

# Check the type of the vaues stored in numpy array
a.dtype

# Create numpy array
c = np.array([20,1,2,3,4])
c

# Assign the first element to 100

c[0] = 100
c

# Assign the 5th element to 0

c[4] = 0
c

# SLICING the numpy array
d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c

arr = np.array([1,2,3,4,5,6,7])
print("[start:end:step]")
print(arr[1:5:2]) # NOTE: We can also define the steps in slicing, like this: [start:end:step].

print(arr[:4]) # NOTE: If we do not pass start its considered 0
print(arr[4:]) # NOTE: If we don't pass end it considers till the length of array.
print(arr[1:5:]) # NOTE: If we don't pass step its considered 1
