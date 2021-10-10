'''
 circular control structure
        loop : while  , for
'''
# i=1
# while i<50:
#     print(i)
#     i +=10
# no=int(input("Enter No:"))
# while no!=0 :
#     print(no)
#     no=int(input("Enter No:"))
# no=int(input("Enter No:"))
# n=1
# mul=1
# while n<=no:
#     mul=mul*n
#     n +=1
#
# print("Factorial :",mul)

no=int(input("Enter No:"))
n=1
m=1
while n<=(2*no-1):
    j=no+1
    while j>=1:
        if j>m:
            print(end=" ")
        else :
            print(j,end=" ")
        j-=1
    if n<no:
        m=m+1
    else:
        m=m-1
    print("")
    n+=1









