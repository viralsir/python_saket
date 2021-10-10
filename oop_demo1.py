'''

    class  : is a bunch of related data.
    object : is a unique medium to access or get the data from related bunch (class).
    no=1
    no=[]
    no={"name":3334,"address":"shahpur"}
    class student{ name , address}

        student(name=vimal,address=")
        student(name=vishal)
        student()


'''
class student:
     #rollno=0
     #name=""

     #constructor
     def __init__(self,rollno=0,name=""):
         self.rollno=rollno
         self.name=name


     def entry(self):
          self.rollno = int(input("Enter Roll No:"))
          self.name = input("Enter Name :")

     def view(self):
          print("roll No:", s.rollno)
          print("Name :", s.name)


studentlist=[]

for i in range(2):
     s=student()
     s.entry()
     studentlist.append(s)


for s in studentlist:
   s.view()




# s1=student()
# s2=student()
#
# s1.rollno=int(input("Enter Roll No:"))
# s1.name=input("Enter Name:")
# print("Roll No:",s1.rollno);
# print("Name :",s1.name)
#
# s2.rollno=int(input("Enter Roll No:"))
# s2.name=input("enter Name :")
# print("Roll No:",s2.rollno);
# print("Name :",s2.name)

