# Python program to find H.C.F of two numbers

num1 = input("enter the first number:")
num2 = input("enter the second number:")
num1 = int(num1)
num2 = int(num2)

# define a function
def computehcf(num1, num2):
    
# choose the smaller number
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            hcf=i
    return hcf

print("the hcf of",num1,"and",num2,"is",computehcf(num1,num2))