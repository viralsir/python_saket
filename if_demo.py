'''
    control structure if
    syntax :
        if condition :
            statement
        else :
            statement

        relational operator
        operator            symbol
        greater than        >
        less than           <
        equal to            ==
        not equal to        !=
        greater than
        or equal to         >=
        less than
        or equal to         <=

        logical operator
        operator        symbol
        and                and
        or             or
        not             not
'''
no1=int(input("Enter No1:"))
no2=int(input("Enter No2:"))
no3=int(input("Enter No3:"))

if no1>0 and no2>0 and no3>0 :

    if no1>no2 and no1>no3:
        print(no1," is a maxium no")
    elif no2>no1 and no2>no3 :
        print(no2," is a maximum no")
    else :
        print(no3," is a maximum no")
else :
    if no1<0:
        print(no1," is a invalid")
    elif no2<0:
        print(no2," is a invalid")
    else :
        print(no3," is a invalid")
    #print("invalid input")




