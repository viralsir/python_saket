'''


     function - def
                         def <defname>(parameter,parameter):
                                    return

     1) define defination
     2) call the def

 1) def with argument and with return value
 2) def with argument and without return value
 3) def without argument and with return value
 4) def without argument and without return value

'''
# def with argument and with return value
# def total(no1,no2):
#     return no1+no2

# def sub(no1,no2):
#     return no1-no2

#def with argument and without return value
# def total(no1,no2):
#     print("Total :",no1+no2)

# def sub(no1,no2):
#     print("sub :",no1-no2)



n1=int(input("Enter No1:"))
n2=int(input("Enter No2:"))

#def without argument and with return value
# def total():
#     return n1+n2

# def sub():
#     return n1-n2


#def without argument and without return value
def total():
    print("total :",n1+n2)

def sub():
    print("sub:",n1-n2)



# total(n1,n2)
# sub(n1,n2)
# print("total :",total(n1,n2))
# print("sub :",sub(no2=n2,no1=n1))
# print("total :",total())
# print("sub:",sub())
total()
sub()