import numpy as np

#Python list 
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#Convert to np.ndarray
a = np.array(a)
b = np.array(b)

print("a: ", a)
print("b: ", b)

#Checking the type of a and b

print("Type of a: ", type(a))
print("Type of b: ", type(b))

#Math Operation

a = np.array([1,2,3,4,5])
b = np.array([2,2,3,6,1])

print("Sum: ", a+b)
print("Difference: ", a - b)
print("Product: ", a * b)
print("Quotient: ", a / b)

#Conditional Operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 2, 3, 6, 1])

print("a==a:", a==a)
print("a==b:", a==b)
print("a>b:", a>b)
print("Type of a==b:", a==b)

#array 2D
a = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print(a)
print("shape:", a.shape) # Returns a tuple representing the shape of array a
