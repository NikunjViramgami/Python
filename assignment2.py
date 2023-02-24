list=[]
while True:
    print("****Subject_Details****")
    print("1.Add Subjects")
    print("2.Remove Subjects")
    print("3.Reverse Subjects")
    print("4.Display Subjects")
    print("5.Count Subjects")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Add subjects")
        num_of_sub=int(input("Enter your count:"))
        print("num_of_sub")
        for i in range(0,num_of_sub):
            subject=input("Enter the subject:")
            list.append(subject)
        print(list)
    if choice==2:
        print("Remove subjects")
        rem_sub=input("Enter your subject you want to delete:")
        for i in list:
            if rem_sub==i:
                list.remove(i)
    if choice==3:
        print("Reverse subjects")
        list.reverse()
        print(list)
    if choice==4:
        print("Display subjects")
        print(list)
    if choice==5:
        print("Count subject")
        print(len(list))
        print(list)

    if choice==6:
        exit()