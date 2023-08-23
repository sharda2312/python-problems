exp=[2200,2350,2600,2130,2190]
# question 1: In Feb, how many dollars you spent extra compare to January?
print("extra spent in Feb compare to january is",exp[1]-exp[0],"dollar.")


# question 2: Find out your total expense in first quarter (first three months) of the year.
print("expense in first quarter is",exp[0]+exp[2]+exp[3])


# queation 3: Find out if you spent exactly 2000 dollars in any month
if (2000 in exp):
    print("if have spent 2000 dollars in one of first five month")
else:
    print("i haven't spent exact 2000 dollars in first five month of this year.")

# question 4: June month just finished and your expense is 1980 dollar.
# Add this item to our monthly expense list
exp.append(1980)
print("june expense is", exp[5])


# queation 5: You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3]=exp[3]-200
print("updated april expense is",exp[3])
