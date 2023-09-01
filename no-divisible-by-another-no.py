# program to find numbers of a list divisible by 13

mylist = [12,25,63,21,39,102,54]
num = 13
result = list(filter(lambda x:x%num==0, mylist))
print("number divisible by", num,"are",result)