# Create a 2D Numpy Array

# Import the Libraries

import numpy as np

# Create a list

a = [[11,12,13], [21,22,23],[31,32,33]]
a

# Convert list to Numpy Array (CAST)
# Every statement is the same type

A = np.array(a)
A

# Show the numpy array dimensions
A.ndim

# Show the numpy array shape
A.shape

# Show the numpy array size
A.size

# Access the element on the first row and first column
A[0][0]

# Access the element on the first row and first and second columns
A[0][0:2]

# Access the element on the first and second rows and third column
A[0:2, 2]
