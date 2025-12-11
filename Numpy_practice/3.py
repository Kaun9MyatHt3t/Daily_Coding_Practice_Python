# From a 2D array of shape ( 5,5) , extract the last row and last column as a separate 1D array

import numpy as np

a = np.arange(25).reshape(5,5)
print(a)
# last row
print(f"last row : {a[-1,]}")
# last column
print(f"last column : {a[:,-1]}")