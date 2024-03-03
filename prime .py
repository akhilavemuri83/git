def is_prime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

num=17
if is_prime(num):
    print(f"{num}is a prime number.")
else:
    print(f"{num}is not a prime number.")



def is_prime(num):
      if num<=1:
	   return False
      for i in range(2,int(num**0.5)+1):
	   if num%i==0:
		return False
      return True
num=int(input("Enter a number:"))
res=is_prime(num)
print(f"{num} is prime: {res}")