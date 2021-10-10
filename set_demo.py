set1={1,2,3,4,5}
set2={3,4,5,6,7,8}
# print(set1)
# set1.add(int(input("enter No:")))
# print(set1)
# set1.remove(4)
# print(set1)
#
# print("no of elements :",len(set1))
# for element in set1:
#     print(element)

print("set1:",set1)
print("set2:",set2)
set3=set1.intersection(set2)  # set1 & set2
print("intersections:",set3)
set3=set1.difference(set2)    # set1 - set2
print("difference :",set3)
set3=set1.union(set2)   # set1 | set2
print("union :",set3)
set3=set1.symmetric_difference(set2) # set1 ^ set2
print("symmentric_deifference:",set3)



