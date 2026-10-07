import numpy as np

a = np.array([1,5,10, 3,4,25,30])

def homework(a):
    condition = ((a % 5 == 0) & (a % 2 == 1))
    return a[condition]

result = homework(a);
print(result)