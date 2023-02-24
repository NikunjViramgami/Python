a=input("Enter String:")
while True:
    print("1.REplace python with Nosql")
    print("2.convert string into list where each word is list item and display with index number")
    print("3.count digit is string")
    print("4.count alphabets in string")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        x=a.replace("Python","Nosql")
    
    if choice==2:
        print("convert string")
        ls=a.split()
        print(ls)
        for i in ls:
            print(i)
    if choice==3:
        print("count digit in string")
        digit=0
        for i in a:
            if i.isdigit():
                digit=digit+1
        print("Digit is:",digit)
    if choice==4:
        print("count alphabets in string")
        letter=0
        for i in a:
            if(i.isalpha()):
                letter=letter+1
        print("Number of Alphabets is",letter)
    if choice==5:
        exit()

