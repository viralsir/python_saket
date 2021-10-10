# dict1={12:12,"second":2,"third":2}
# print(dict1["second"])
# print(dict1["third"])
# print(dict1.get(12))
# person={"name":"viral","address":"naranpura","phno":[955896955,7698261]}

person={"name":"vimal"}
person["first_name"]="1223"

print(person)
# person_list=[]
# person={"name":"viral","address":"naranpura","phno":{"home":955896955,"office":7698261}}
# person_list.append(person)
person1={"name":"vishal","address":"naranpura","phno":{"home":955896955,"office":7698261}}
print(person1)
print(person1.keys())
print(person1.values())
print(person1.items())

for key in person1.keys():
    print(key)

for value in person1.values():
    print(value)

for key,value in person1.items():
    print(key,value)

# person_list.append(person1)
# print(person_list[0]["phno"]["home"])

# print(person["name"])
# print(person["address"])
# print(person["phno"])
# person["phno"]["home"]=9879299590
# print(person["phno"])