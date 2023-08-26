# find numbers divisible by another number.

def divisible(l1,num):
    l2=[]
    for j in l1:
        if j%num==0:
            l2.append(j)
    print("numbers divisble by",num,"is/are",l2)
               
l3=[5,10,56,53,51,14,41,20,31,39,37,36,32,0]
divisible(l3,2)

    
    
    
# end def