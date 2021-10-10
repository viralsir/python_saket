start=True
while start==True:
    try:
        number1=int(input("Enter No1:"))
        number2=int(input("Enter No2:"))

        ans=number1/number2
        print("ans:",number1/number2)
        start=False
    except ZeroDivisionError:
         print("zero is invalid as a second no")
    except ValueError :
        print("charactare are not allowed")
    finally:
        print("finally statement is executed")


