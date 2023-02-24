# v1=int(input("Enter num1:"))
# v2=int(input("Enter num2:"))
# v3=v1+v2
# print("Sum:",v3)

# v1="My Name is Nikunj"
# print(v1[1:5])
# print(v1[:])
# print(v1.endswith("Nikunj"))
# print(v1.upper())
# print(v1.lower())
# print(v1.count("N"))
# print(v1.capitalize())
# print(v1.replace("Nikunj","Raj"))

# n1=[2,4,5,6,78,9]
# print(n1)
# n1.sort()
# print(n1)
# n1.reverse()
# print(n1)
# print(min(n1))
# print(max(n1))
# n1.append(10)
# print(n1)
# n1.insert(1,33)
# print(n1)
# n1.remove(10)
# print(n1)

# mutable-can change, list
# immutable-can not change, tupple

# t1=(1,2,3)
# t1[0]=5
# print(t1)

#swap function
# a1=1
# a2=4
# a1,a2=a2,a1
# print(a1,a2)

#dictionary

# d1={"name":"Nikunj","salary":20000,"Designation":"QA","Hobby":{"Cricket","song","Reading"},"report":{"A":"Positive","B":"Negative"}}
# d1["fname"]="Viramgami"
# print(d1["report"])
# d1.update({"festival":"Holi"})
# print(d1)
# del d1["Hobby"]
# print(d1)
# print(d1.keys())
# print(d1.values())
# d2=d1.copy()
# del d2["fname"]
# print(d2)
# print(d1)

# dic={"mutable":"meand chamnge","immutable":"means not change","like":"Love the way uhh like","Love":"Beautiful feeling in the world"}
# a1=input("Enter the words you want to know in particular mean:")
# print(dic[a1])

# s=set()
# s.add(1)
# s.add(2)
# #its usee not dubplicate value repeat only unique value given
# # s1=s.intersection({1,2,3})
# s1=s.union({1,2,3})
# print(s,s1)

# v1=2
# v2=9
# v3=int(input())
# if v3>v2:
#     print("greater")
# elif v3==v2:
#     print("Equal")
# else:
#     print("lesser")

# list=[1,2,3]
# print(7 not in list)
# if 7 not in list:
#     print("yes")

# s1=int(input("Enter your Age:"))
# if 7<s1<100:
#     if s1>18:
#         print("licence applied")
#     elif s1==18:
#         print("Not decided")
#     else:
#         print("Not valid")

#faulty calculator
#45*3=555,56+9=77,56/6=4

# a1=input("Enter the operator:")
# v1=int(input("Enter the value1:"))
    
# v2=int(input("Enter the value2:"))

# if a1=="+" and v1==56 and v2==9:
#     print("77")
# elif a1=="*" and v1==45 and v2==3:
#     print("555")
# elif a1=="/" and v1==56 and v2==6:
#     print("4")
# elif a1=="+":
#     v3=v1+v2
#     print(v3)
# elif a1=="-":
#     v3=v1-v2
#     print(v3)
# elif a1=="*":
#     v3=v1*v2
#     print(v3)
# elif a1=="/":
#     v3=v1/v2
#     print(v3)
# else:
#     exit()


# list=[str,int,"Harry",1,2,56,89,7,3]
# for i in list:
#     if str(i).isnumeric() and i>=6:
#         print(i)
# while True:
#     num=int(input("Enter your num:"))

#     # if num<100:
#     #     i=i+1
#     #     continue
#     if num>100:
#         print("Congrats")
#         break
#     else:
#         continue
        
# num=18
# num_of_Guusses=1
# print("You have only 9 attemp to gusees correct number")

# while num_of_Guusses<=9:
#     guess_Number=int(input("Enter your number:"))
#     if guess_Number<18:
#         print("You have to choose smaller number! Please choose high number\n")
#     elif guess_Number>18:
#         print("You choose higher number! plzz chosse lower number\n")
#     else:
#         print("You won\n")
#         print(num_of_Guusses,"No of attemp to finish the game:")
#         break
#     print(9-num_of_Guusses,"No of gusses left")
#     num_of_Guusses=num_of_Guusses+1

# if(num_of_Guusses>9):
#     print("Game over")

#docstring

# def function(a,b):
#     """this is a function to two num of sum"""
#     average=(a+b)/2
#     return average

# v=function(5,7)
# print(v)
# print(function.__doc__)

# num1=input("Enter num1:")
# num2=input("Enter num2:")
# try:
#     print("The sum of two number is: ",int(num1)+int(num2))
# except Exception as e:
#     print(e)
#     print("This line is true")

# f=open("y.txt","w")
# f.write("My name is nikunj\n")
# f.write("Hobby is cricket")
# f.close()

# f=open("y.txt","r")
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()

# f=open("y.txt","r")
# print(f.readline())
# print(f.seek(10))
# print(f.readline())
# f.close()
# x=96
# def nik():
#     x=20
#     def rohan():
#         global x
#         x=25
#     print("Before calling rohan()",x)
#     rohan()
#     print("After calling rohan()",x)
# nik()
# print(x)

# def factorial(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact

# def factorial_recursion(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_recursion(n-1)
# n=int(input("Enter the Number:"))
# print("without recursion",factorial(n))
# print("with recursion",factorial_recursion(n))

# def fibonaci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)

# n=int(input("Enter the number:"))
# print(fibonaci(n))

# a=int(input("how many rows uhh have printed:"))
# b=bool(int(input("Enter 0 or 1:")))
# if b:
#     for i in range(1,a+1):
#         print("\n")
#         for a in range(i):
#             print("*",end='')
# else:
#     for i in range(a,0,-1):
#         print("\n")
#         for a in range(i):
#             print("*",end="")

# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             value=input("type here\n")
#             f=open("harry.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()
#         if c==2:
#             value=input("type here\n")
#             f=open("harry.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()
#     elif k==2:
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             value=input("type here\n")
#             f=open("nikunj.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()
#         if c==2:
#             value=input("type here\n")
#             f=open("nikunj.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()
        
#     elif k==3:
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             value=input("type here\n")
#             f=open("karan.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()
#         if c==2:
#             value=input("type here\n")
#             f=open("karan.txt","a")
#             f.write(str([str(gettime())])+":"+value+"\n")
#             print("Written successfully")
#             f.close()

#     else:
#         print("Enter valid input")
# def retrieve(k):
#     if k==1:
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             f=open("harry.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#         if c==2:
#             f=open("harry.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#     elif k==2:
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             f=open("nikunj.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#         if c==2:
#             f=open("nikunj.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#     elif k==3:
        
#         c=int(input("Enter 1 for exercise 2 for food:"))
#         if c==1:
#             f=open("karan.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#         if c==2:
#             f=open("karan.txt","r")
#             for i in f:
#                 print(i)
#             f.close()
#     else:
#         print("Please enter valid inputs")
# def delete(k):
#     if k==1:
#         c=int(input("press 1 for exercise 2 for food"))
#         if c==1:
#             f=open("harry.txt","r")
#             rem=input("Enter you want to remove exercise:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("harry.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#         if c==2:
#             f=open("harry.txt","r")
#             rem=input("Enter you want to remove food:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("harry.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#     elif k==2:
#         c=int(input("press 1 for exercise 2 for food"))
#         if c==1:
#             f=open("nikunj.txt","r")
#             rem=input("Enter you want to remove exercise:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("nikunj.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#         if c==2:
#             f=open("nikunj.txt","r")
#             rem=input("Enter you want to remove food:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("nikunj.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#     elif k==3:
#         c=int(input("press 1 for exercise 2 for food"))
#         if c==1:
#             f=open("karan.txt","r")
#             rem=input("Enter you want to remove exercise:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("karan.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#         if c==2:
#             f=open("karan.txt","r")
#             rem=input("Enter you want to remove food:")
#             res=f.readlines()
#             f.close()
#             for i in res:
#                 if rem in i:
#                     res.remove(i)
#             f=open("karan.txt","w")
#             for i in res:
#                 f.write(i)
#             f.close()
#     else:
#         print("plzz Enter valid inputs")

#    print("Health management system")
# a=int(input("press 1 for lock the value nd 2 for retrieve 3 for delete"))
# if a==1:
#     b=int(input("1 for harry 2 for nikunj 3 for karan"))
#     take(b)
# elif a==2:
#     b=int(input("1 for harry 2 for nikunj 3 for karan"))
#     retrieve(b)
# elif a==3:
#     b=int(input("1 for harry 2 for nikunj 3 for karan"))
#     delete(b)
# else:
#     print("plzz enter valid inputs")


# module

# import random
# random_Number=random.randint(0,8)
# print(random_Number)
# ran=random.random()
# print(ran)
# list=["nk","hu","ik"]
# choice=random.choice(list)
# print(choice)
# list=['nik','aman','om']
# for index,item in enumerate(list):
#     if index%2==0:
#         print(index)

# def fac(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     return fact
# n=int(input("Enter the number:"))
# print(fac(n))

# def fibonaki(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     else:
#         return fibonaki(n-1)+fibonaki(n-2)
# n=int(input("Enter the Numbr:"))
# print(fibonaki(n))

# Join Function use
# list=["randy","orton","john","cena"]
# a=",".join(list)
# print(a)

#map function to use string to conver int
# numbers=["1","2","3"]
# numbers=list(map(int,numbers))
# numbers[2]=numbers[2]+1
# print(numbers)

# def sq(n):
#     return n*n
# num=[2,3,4,5,6,7,8,9]
# square=list(map(sq,num))
# print(square)


# num=[2,3,4,5,6,7,8,9]
# square=list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a
# def cube(a):
#     return a*a*a
# fun=[square,cube]
# for i in range(5):
#     num=list(map(lambda x:x(i),fun))
#     print(num)

# filter function
# list_1=[1,2,3,4,5,6,7,8,9]
# def lessthan_5(num):
#     return num<5

# lt_5=list(filter(lessthan_5,list_1))
# print(lt_5)
# 

# from functools import reduce
# list_1=[1,2,3,4,5,6,7,8,9,0]
# num=reduce(lambda x,y:x+y,list_1)
# print(num)

# import random
# lst=["s","w","g"]

# chance=10
# No_Of_Chance=0
# computer_point=0
# human_point=0
# print("\t\t\t snake,water,gun\n\n\n")
# print("s for snake")
# print("g for gun")
# print("w for water")
# while No_Of_Chance<chance:
#     user=input("snake,water,gun:")
#     _random=random.choice(lst)

#     if user=="s" and _random=="g":
#         computer_point=computer_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("Computer wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user=="s" and _random=="w":
#         human_point=human_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("human wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user=="w" and _random=="s":
#         computer_pount=computer_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("computer wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user=="w" and _random=="g":
#         human_point=human_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("human wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user=="g" and _random=="w":
#         computer_pount=computer_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("computer wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user=="g" and _random=="s":
#         human_point=human_point+1
#         print(f"computer have choice {_random} and use have choose {user}\n")
#         print("human wins 1 point\n")
#         print(f"computer point is{computer_point} and your point is {human_point}")

#     elif user==_random:
#         print("point is tied ")

#     else:
#         print("user have take wrong input")

#     No_Of_Chance=No_Of_Chance+1
#     print(f"{chance-No_Of_Chance} if left out with {chance}\n")

# print("game over")

# if computer_point>human_point:
#     print("computer wins and uhh lose")
# elif human_point>computer_point:
#     print("You won nd computer lose")
# else:
#     print("tie")

# print(f"your point is{human_point} and computer point is {computer_point}")

# def dec1(fun1):
#     def nowexec():
#         print("function is executing")
#         fun1()
#         print("Executed")
#     return nowexec

# @dec1

# def nikunj():
#     print("Nikunj is a good boy")
# nikunj=dec1(nikunj)
# nikunj()

# class Employee:

#     No_Of_leaves=8
#     def __init__(self,name,salary,age):
#         self.name=name
#         self.salary=salary
#         self.age=age

#     def Printdetails(self):
#         print(f"the name is {self.name}  salry is {self.salary} age is {self.age}")



#     @classmethod
#     def changeleave(cls,newleaves):
#         cls.No_Of_leaves=newleaves


# rohan=Employee("nikunj","52000","52")
# harry=Employee("Harry","85000","67")
# rohan.changeleave(52)
# print(rohan.No_Of_leaves)

#Armstrong Number
# print('Enter twonumber betwwen 100 to 999')
# a=input()
# b=input()
# for i in range(int(a),int(b)):
#     no=str(i)
#     arm=int(no[0])**3+int(no[1])**3+int(no[2])**3
#     if arm==int(no):
#         print('Armstrong no',no)
#         i=i+1

#basics programming in python

# print("Hello.")
# a=10
# b=20
# c=a+b
# print('Sum:',c)

#Area of Triangle
# a=5
# b=9
# c=10
# s=(a+b+c)/2
# print(s)
# Area=s*(s-a)+s*(s-b)+s*(s-c)
# print('Area of triangle',Area)

#swap in two numbers

# a=10
# b=20

# a,b=b,a

# print('The value of a after swapping a:',a)
# print('The value of a after swapping b:',b)

#check the number is positive,negetive or zer0

# value=int(input('Enter the Number:'))
# if value>0:
#     print('Postive')
# elif value<0:
#     print('Negetive')
# elif value==0:
#     print('Zero')

#check the Number is odd or even

# Num=int(input('Enter the Number:'))
# if Num%2==0:
#     print('Even Number')
# else:
#     print('Odd Number')

#pattern

# for num in range(5):
#     for i in range(num):
#         print(num,end=' ')
#     print('\n')

#prime Number
# num=int(input('Enter the Number:'))
# flag=False
# if num==1:
#     print(num,'Not a Prime Number')
# elif num>1:
#     for i in range(2,num):
#         if num%i==0:
#             flag=True
#             break
#     if flag:
#         print(num,'is not a prime Number')
#     else:
#         print(num,'is prime Number')

#lip Year

# year=int(input('Enter the Year:'))
# if (year%400 == 0) and (year%100==0):
#     print(year,'is a lip Year')
# elif (year%4==0) and (year%100!=0):
#     print(year,'is a lip Year')
# else:
#     print(year,'is not a Lip Year')

#print all prime Number

# lower=2
# upper=100

# print('Prime Number is',lower,'and',upper,'are:')

# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

# Find Factorial of given Number

# num=int(input('Enter the Number:'))
# factorial=1

# if num < 0:
#     print('Number is Not Factprial')
# elif num == 0:
#     print('Factorial of 0 is 1')
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i

#     print('The Factorial of',num,'is',factorial)

# num=int(input('Enter the number :'))

# for i in range(1,11):
#     print(num,'x',i,'=',num*i)

#fibonaci 0,1,1,2,3,5,8

# Terms=int(input('Enter the Term:'))
# n1=0
# n2=1
# count=0
# if Terms<=0:
#     print('Please select positive term')
# elif Terms==0:
#     print(n1)
# else:
#     print('Fibonaki series')

#     while count<Terms:
        
#         print(n1)
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         count+=1

num=int(input('Enter the Number:'))

if num< 0:
    print('Please take positive number')
else:
    sum=0
    while num > 0:
        sum+=num
        num-=1
    print('The sum is',sum)
    





        


