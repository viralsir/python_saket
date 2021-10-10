'''
    inheritance : is the proccess by which object of one class access or get the properties of another class
    single inheritance :  one object can access or get the properties of only one object at a time.
                            a
                            |
                            b
    multilevel inheritance : continous chain of single inheritance .
                            a
                            |
                            b
                            |
                            c
    hyrarchical inheritance :more than one object can access the properties of same object
                          a personal_info
                    |           |
         (student)  b           c (teacher)

    multiple Inheritance : one object can access or get the properties of more than object

                               a                b
                                      |
                                      c

    hybrid inheritance : combination of more than one inheritance

                                  a  personal_info
                            |           |
                   student b           c  teacher
                                 |
                                 d  school

'''
class Personal_Info:
    name=""
    phno=""

    def set_personal_info(self):
        self.name=(input("Enter Name :"))
        self.phno=input("Enter Phno:")

    def get_personal_info(self):
        print("Name :",self.name)
        print("Phno :",self.phno)


class student(Personal_Info):
     rollno=0
     std=1

     def set_student(self):
         self.set_personal_info()
         self.rollno=int(input("Enter Roll No:"))
         self.std=int(input("Enter Std :"))

     def get_student(self):
         self.get_personal_info()
         print("Roll no:",self.rollno)
         print("Std:",self.std)


class Teacher(Personal_Info):
     salary=0

     def setsalary(self):
         self.set_personal_info()
         self.salary=int(input("Enter Salary:"))

     def getsalary(self):
        self.get_personal_info()
        print("Salary :",self.salary)


class school(student,Teacher):
    board=""

    def set_school(self):
        self.set_student()
        self.board=input("Enter School Board")

    def get_school(self):
        self.get_student()
        print("school board :",self.board)





s1=student()
t1=Teacher()

s1.set_student()
t1.setsalary()

s1.get_student()
t1.getsalary()

# s1=school()
# #s1.set_personal_info()
# #s1.set_student()
# s1.set_school()
#
# #s1.get_personal_info()
# #s1.get_student()
# s1.get_school()
