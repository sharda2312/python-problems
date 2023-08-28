# Python program to find the factorial of a number provided by the user.

num = input("enter the number:")
num = int(num)
factorial=1
if num==0:
    print("factorial of 0 is 1")
else:
    for j in range(1, num+1):
        factorial=factorial*j
   
    print("factorial of", num, "is", factorial)    