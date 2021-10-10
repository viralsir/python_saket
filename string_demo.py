'''
 string is a immutable list
'''

name="vimal is a good boy."
name=input("enter Name:")


for character in name:
    print(character)

# words=name.split("i")
# print(words)

# name=name.upper()
# print("name1:",name)
# print("name:",name)
# print("upper case :",name.upper())
# print("lower case :",name.lower())
# print("title case :",name.title())
# print("Captlization :",name.capitalize())
# name="vimal" + "shah"
# name="vimal"*2
# if name.islower() :
#     print("name is in lower case")
# elif name.isupper():
#     print("name is in upper case")
# elif name.istitle():
#     print("name is in title case ")

if name.isalpha():
    print("name has all the characters ")
elif name.isnumeric():
    print("name has all the numbers ")
elif name.isalnum():
    print("name has character and number both ")
else :
    print("name has character  ,number and symbols")
print(name)

# print(name[:5])
# name[0]='r'
# print(name)
