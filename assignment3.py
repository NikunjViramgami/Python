Restaurant=[]
while True:
    print("****Restaurant_Details****")
    print("1.Manage details")
    print("2.Display details")
    print("3.Delete records")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Manage details")
        dict={}
        dict["Name"]=input("Enter restuarant name:")
        dict["cuisine"]=input("Enter restuarant capacity:")
        dict["Rating"]=input("Enter restuarant price:")
        dict["Location"]=input("Enter restuarant location:")
        print(dict)
        Restaurant.append(dict)
    if choice==2:
        print("display details")
        print('Name',"    \t",'Cuisine',"   \t",'Rating',"    \t",'Location')
        for i in Restaurant:
            print(i['Name'],"    \t",i['Cuisine'],"    \t",i['Rating'],"    \t",i['location'])
    if choice==3:
        for i  in Restaurant:
            print("Cuisine and Rating Records Are Deleted as per the given Criteria")
            print("press 1 for Yes")
            print("press 2 for No")
            user=int(input("Delete the record of Cuisine and Rating:"))	
            if i['Cuisine']=='Chinese' and i['Rating']<3.5:
                del i['Cuisine'] 
                del i['Rating']
                print(i)
            else:
                print("No Records Are Deleted")
                print(Restaurant)
    if choice==4:
        exit()