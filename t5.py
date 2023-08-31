import numpy as np


numbers = input("Enter the numbers")
new=numbers.split()
arr=np.array(new,dtype=float)
print(arr)
res = arr[::-1]
print(res)


