list1=[]
while True:
    print("1.Add student")
    print("2.Remove student")
    print("2.Display student")
    print("2.Student with highest percentage")
    print("2.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Add students")
        dic={}
        dic["Rollno"]=int(input("Enter your rollno:"))
        dic["Name"]=input("Enter your name:")
        dic["sub1"]=int(input("Enter your marks:"))
        dic["sub2"]=int(input("Enter your marks:"))
        dic["sub3"]=int(input("Enter your marks:"))
        dic["total_marks"]=dic["sub1"]+dic["sub2"]+dic["sub3"]
        print(dic)
        list1.append(dic)
    if choice==2:
        print("Remove student")
        rem_stu=input("Enter name you want to remove:")
        for i in list1:
            if rem_stu==i["Name"]:
                list1.remove(i)
    if choice==3:
        print("Display student")
        print(list1)
    if choice==4:
        print("Student with highest percentage")
        percentage=dic["total_marks"]/3
        highest=0
        for i in list:
            if percentage>highest:
                highest=i["total_marks"]
                student=i["Name"]
                print(i["Name"],"Highest percentage is",percentage)

    if choice==5:
        exit()