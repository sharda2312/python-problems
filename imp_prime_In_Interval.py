# Python program to display all the prime numbers within an interval


num1=input("enter the start number")
num2= input("enter ending number")

num=range(int(num1), int(num2))
for i in num:
    if i>1:
    
        for j in range(2, i):
            if i%j==0:
                break
            
        else:
            print(i,"is a prime")
            
                       
                    
             