# Your monthly expense list (from Jan to May) looks like this,

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
# Write a program that asks you to enter an expense amount and program should 
# tell you in which month that expense occurred. If expense is not found then 
# it should print that as well.

ex = input("Please enter expense amount: ")
ex=int(ex)

month=-1
for i in range(len(expense_list)):
    if (ex==expense_list[i]):
        month=i
        break

if (month!=-1):
    print(f'You spent {ex} in {month_list[month]}')
else:
    print(f'You didn\'t spend {ex} in any month')