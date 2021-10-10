Student_List=[]
subject=["Maths","Science","English","Phy"]
Std=[{"A":[{},{},{}],"B":[{},{},{},{}]},{"A":[{},{},{}],"B":[{},{},{},{}]},]
Student_Div={"A":[{},{},{}],"B":[{},{},{},{}]}

#std[1]["B"][5]["name"]
Student_Div["A"][0]["name"]
op=1
while op !=3 :
    print("\t\t Student Info")
    print("\t press 1 for Entry ")
    print("\t press 2 for View ")
    print("\t press 3 for Exit ")

    op=int(input("Enter Your Option :"))

    if op==1:

        for i in range(3):
            student={}
            student["rollno"]=(int(input("Enter Roll No:")))
            student["name"]=input("Enter Name :")

            for sub in subject:
                mark=int(input("Enter "+sub+" Marks:"))
                while not 0<=mark<=100 :
                    print("invalid marks")
                    mark = int(input("Enter "+sub+" Marks:"))
                student[sub]=mark
            Student_List.append(student)
            # [{"name":vimal,"Maths":23,"English":23},{"name":"vishal","maths":23},{}]
    elif op==2:
        for student in Student_List:
            print("\n output :\n")
            print("Roll No:",student["rollno"])
            print("Name :",student["name"])
            total=0
            for sub in subject:
                print(sub,student[sub])
                total += student[sub]

            print("Total :",total)
    elif op==3:
        print("you are exited ")
    else :
        print("wrong option selected try again !!")
