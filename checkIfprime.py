# Program to check if a number is prime or not

num = input("enter the number:")
num = int(num)
i = 2
while i < num:
   if num % i == 0:
      print("number is not prime")
      break
   i = i+1
      
else:
   print("is prime number")   
    
