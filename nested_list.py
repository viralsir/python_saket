list1=[23,44,55,66,[[44,55],66]]
list2=[3,6]


 

# list3=list2+list1
# list4=list1*2
# print(list1)
# print(list2)
# print(list3)
# print(list4)
list1.append(list2[:])
list2.append(7)
print(list1[-2][0][0])
print(list2)