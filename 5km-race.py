# Lets say you are running a 5 km race. Write a program that,

# 1: Upon completing each 1 km asks you "are you tired?"
# 2: If you reply "yes" then it should break and print "you didn't finish the race"
# 3: If you reply "no" then it should continue and ask "are you tired" on every km
# 4: If you finish all 5 km then it should print congratulations message


print("your 5 km race started....")
for i in range(1,6):
    
    if (i<5):
        print(f"{i} km completed are you tired? Reply in only yes/no")
        ans = input()
        if (ans=='yes'):
            print("you didn't finish the race") 
            break
        elif (ans=='no'):
            continue
        else:
            print("please reply only in yes/no")
    print("congratulations you successfully completed the race")