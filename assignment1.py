list=[]
while True:
    print("****Garbaclub****")
    print("1.Add Details")
    print("2.Search Details")
    print("3.Exit")
    choice=int(input("Enter your chioice:"))
    if choice==1:
        print("Add Details")
        dic={}
        dic["Garbaclub_Name"]=input("Enter name:")
        dic["Garbaclub_Capacity"]=int(input("Enter capacity:"))
        dic["Garbaclub_Price"]=int(input("Enter price:"))
        dic["Garbaclub_Location"]=input("Enter location:")
        print(dic)
        list.append(dic)
        for i in list:
            print(i["Garbaclub_Name"])
            print(i["Garbaclub_Capacity"])
            print(i["Garbaclub_Price"])
            print(i["Garbaclub_Location"])

    if choice==2:
        print("Search Details")
        location=input("Enter your location:")
        capacity=int(input("Enter your capacity:"))
        for i in list:
            if i["Garbaclub_Location"]==location and i["Garbaclub_Capacity"]>5000:
                print(i)
            else:
                print("No match found")
    if choice==3:
        exit()
