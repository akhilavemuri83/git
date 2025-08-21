import numpy
n=int(input("Enter a number:"))
a=numpy.prod([i for i in range(1,n+1)])
print(a)