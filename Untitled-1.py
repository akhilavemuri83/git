#def is_prime(number):
 #   if number<=1:
  #      return False
   # for i in range(2,int(number**0.5)+1):
    #    if number%i==0:
     #       return False
    #return True

#num=1
#if is_prime(num):
 #   print(f"{num} is a prime number.")
#else:
 #   print(f"{num} is not a prime number.")



def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
           return False
    return True
num=int(input("Enter a number:"))
res=prime(num)
print(f"{num} is a prime number: {res}")



