#def fact(n):
 #   return 1 if (n==1 or n==0) else n*fact(n-1)
#num=7
#print("factorial of ",num,"is",fact(num))

#import numpy
#n=int(input("Enter a number:"))
#a=numpy.prod([i for i in range(1,n+1)])
#print(a)

a=int(input("Enter a number:"))
fact=1
if a<0:
    print("factorial does not exist for negative numbers")
elif a==0:
    print("factorial for 0 is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("the factorial of ", a, "is",fact)