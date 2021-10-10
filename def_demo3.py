def prime(no):
    is_prime=True
    for i in range(2,no):
        if no % i == 0 :
            is_prime=False
    return is_prime

def factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact


# no=int(input("enter No:"))
#
# if prime(no):
#     print(no," is a prime no")
# else :
#     print(no," is not a prime no")
