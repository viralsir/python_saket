#import def_demo3
from def_demo3 import  prime,factorial

for i in range(1,100):
    #if def_demo3.prime(i):
     if prime(i):
        print(i)

print("factorial :",factorial(int(input("enter NO:"))))