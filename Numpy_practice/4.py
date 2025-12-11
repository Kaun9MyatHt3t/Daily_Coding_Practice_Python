# Given an array of random integers from 0 to 50 , select all values that are divisible by 5.

import numpy as np

a = np.random.randint(0,50, size=10)
print(a)
print(a[a % 5 == 0])