start=True
while start==True:
    try:
        no1=int(input("Enter No1:"))
        no2=int(input("Enter No2:"))

        ans=no1/no2
        print("ans:",no1/no2)
        start=False
    except ZeroDivisionError:
         print("zero is invalid as a second no")
    except ValueError :
        print("charactare are not allowed")
    finally:
        print("finally statement is executed")


