# from tkinter import*
# from tkinter import messagebox
# top=Tk()
# top.geometry("200x200")
# def hellocallback():
#     messagebox.showinfo("Hello Python","Hello word")
# b=Button(top,text="Hello",command=hellocallback)
# b.pack()
# top.mainloop()

# import tkinter
# top=tkinter.Tk()
# var1=tkinter.IntVar()
# tkinter.Checkbutton(top,text="Male",variable=var1).grid(row=0,column=1)
# var2=tkinter.IntVar()
# tkinter.Checkbutton(top,text="Female",variable=var2).grid(row=1,column=1)
# top.mainloop()

# from tkinter import*
# top=Tk()
# top.geometry("600x600")
# Label(top,text="FirstName").grid(row=0)
# Label(top,text="Lastname").grid(row=1)
# e1=Entry(top).grid(row=0,column=1)
# e2=Entry(top).grid(row=1,column=1)
# top.mainloop()

# from tkinter import*
# top=Tk()
# l=Listbox(top)
# l.insert(1,"Python")
# l.insert(2,"Java")
# l.insert(3,"Nosql")
# l.insert(4,"ooad")
# l.pack()
# l.mainloop()

# from tkinter import*
# from tkinter import messagebox
# def add():
#     a1=e1.get()
#     a2=e2.get()
#     sum=int(a1)+int(a2)
#     print(sum)
#     Label(a,text="sum"+str(sum)).grid(row=4,column=1)
#     messagebox.showinfo("Add successful")
# a=Tk()
# a.geometry("200x200")
# a.title("Calculator")
# l1=Label(a,text="value1")
# l1.grid(row=0,column=0)
# l2=Label(a,text="value2")
# l2.grid(row=1,column=0)
# e1=Entry(a)
# e1.grid(row=0,column=1)
# e2=Entry(a)
# e2.grid(row=1,column=1)
# b=Button(a,text="Add",command=add)
# b.grid(row=3,column=0)
# a.mainloop()


# from tkinter import*
# from tkinter import messagebox

# def printdetails():
#     a1=e1.get()
#     a2=e2.get()
#     f=open("b.txt","a")
#     f.write("fname is {a1} and password is {a2}")
#     f.close()
#     print(f"name is {a1} and password is {a2}")
#     Label(a,text="name"+str(a1)+"password"+str(a2),bg="brown")
#     messagebox.showinfo("login successful")
# a=Tk()
# a.geometry("200x200")
# a.title("Login")
# a.config(bg="black")
# l1=Label(a,text="name",bg="red")
# l1.grid(row=0,column=0)
# l2=Label(a,text='Password',bg="yellow")
# l2.grid(row=1,column=0)
# e1=Entry(a)
# e1.grid(row=0,column=1)
# e2=Entry(a)
# e2.grid(row=1,column=1)
# b=Button(a,text="Login",command=printdetails)
# b.grid(row=3,column=1)
# b.mainloop()

# v1=input("Enter the name")
# v2=input("Enter the age")
# print(f"name is {v1} and age is {v2}")


# class CoffeCafe:
#     def __init__(self):
#         self.CoffeNo=0
#         self.Price=0
#         self.Size=0

#     def Add(self):
#         self.CoffeNo=input("Enter the coffe no:")
#         self.Price=input("Enter the coffe price:")
#         self.Size=input("Enter the coffe size:")
#         f=open("g.txt","a")
#         f.write((self.CoffeNo)+" "+(self.Price)+" "+(self.Size)+"\n")
#         f.close()
        
#     def display(self):
#         f=open("g.txt","r")
#         for i in f:
#             print(i)
#         f.close()

#     def Delete(self):
#         f=open("g.txt","r")
#         rem=input("Enter Delete coffe No:")

#         res=f.readlines()
#         f.close()

#         for i in res:
#             if rem in i:
#                 res.remove(i)
#         f=open("g.txt","w")
#         for i in res:
#             f.write(i)
#         f.close()

#     def search(self):
#         search=input("Enter the search coffe No:")
#         f=open("g.txt","r")
#         for i in f:
#             if search in i:
#                 print(i)

# c=CoffeCafe()
# while(True):
#     print("1. Add")
#     print("2. Display")
#     print("3. Delete")
#     print("4.search")
#     print("5.Exit")
#     choice=int(input("Enter Your choice:"))
#     if choice==1:
#         c.Add()
#     if choice==2:
#         c.display()
#     if choice==3:
#         c.Delete()
#     if choice==4:
#         print("search successful")
#         c.search()
#     if choice==5:
#         break
        

# c=CoffeCafe()
# from tkinter import*
# from tkinter import messagebox
 
# win=Tk()
# win.geometry("300x300")
# win.title("Coffe")
# l1=Label(win,text="Coffe No:")
# l1.grid(row=0,column=0)
# l2=Label(win,text="Price")
# l2.grid(row=1,column=0)
# l3=Label(win,text="Size")
# l3.grid(row=2,column=0)
# e1=Entry(win)
# e1.grid(row=0,column=1)
# e2=Entry(win)
# e2.grid(row=1,column=1)
# e3=Entry(win)
# e1.grid(row=2,column=1)

# b1=Button(win,text="Add",Command=c.Add)
# b1.grid(row=3,column=3)
# win.mainloop()


from tkinter import messagebox
from datetime import datetime
# from tkinter import*
# from tkinter import messagebox
# class Student:
#     def __init__(self):
#         self.fname=""
#         self.lname=""
#         self.roll_no=""
#         self.mobile_no=""

#     def add(self):
#         self.fname=e1.get()
#         self.lname=e2.get()
#         self.roll_no=e3.get()
#         self.mobile_no=e4.get()
#         print(f"{self.fname} {self.lname} {self.roll_no} {self.mobile_no} at time {datetime.now()}")
#         f=open("dd.txt","a")
#         f.write(f"{self.fname} {self.lname} {self.roll_no} {self.mobile_no} \n")
#         f.close()
#         messagebox.showinfo("title","Add successfully")
#     def search(self):
#         s=e5.get()
#         f=open("dd.txt","r")
#         for i in f:
            
#             if s in i:
#                 print(i)
#                 l7=Label(win,text=i)
#                 l7.grid(row=8,column=3)
#         f.close()

#     def delete(self):
#         s1=e6.get()
#         f=open("dd.txt","r")
#         st=f.readlines()
#         f.close()
#         for i in st:
#             if s1 in i:
#                 st.remove(i)
#                 messagebox.showinfo("title","delete")
#         f=open("dd.txt","w")
#         for i in st:
#             f.write(i)
#         f.close()
            

#     def clear():
#         pass

# s=Student()
# win=Tk()
# win.geometry("500x500")
# win.title("student")

# l=Label(win,text="Student Details",font="ariel 10 bold")
# l.grid(row=0,column=3)

# l1=Label(win,text="fname")
# l1.grid(row=1,column=0)
# l2=Label(win,text="lname")
# l2.grid(row=2,column=0)
# l3=Label(win,text="roll_no")
# l3.grid(row=3,column=0)
# l4=Label(win,text="mobile_no")
# l4.grid(row=4,column=0)

# fname=StringVar()
# lname=StringVar()
# roll_no=StringVar()
# mobile_no=StringVar()

# e1=Entry(win,textvariable=fname)
# e1.grid(row=1,column=1)
# e2=Entry(win,textvariable=lname)
# e2.grid(row=2,column=1)
# e3=Entry(win,textvariable=roll_no)
# e3.grid(row=3,column=1)
# e4=Entry(win,textvariable=mobile_no)
# e4.grid(row=4,column=1)

# b1=Button(win,text="Add",command=s.add)
# b1.grid(row=5,column=3)

# l5=Label(win,text="roll_no")
# l5.grid(row=6,column=0)

# # stu_rollno=StringVar()
# e5=Entry(win)
# e5.grid(row=6,column=1)

# b2=Button(win,text="Search",command=s.search)
# b2.grid(row=7,column=3)

# l6=Label(win,text="roll_no")
# l6.grid(row=9,column=0)

# stu_rollno=StringVar()
# e6=Entry(win,textvariable=stu_rollno)
# e6.grid(row=9,column=1)

# b3=Button(win,text="Delete",command=s.delete)
# b3.grid(row=10,column=3)

# b4= Button(text='Exit',command=quit)
# b4.grid(row=11,column=3)


# win.mainloop()

from tkinter import*
from tkinter import messagebox

class MobileStore:   
    def __init__(self):
        self.Mobile_Name=""
        self.Mobile_Brand=""
        self.Mobile_price=""

    def Add(self):
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        print(f"{a1} {a2} {a3}")
        f=open("love.txt","a")
        f.write(f"{a1} {a2} {a3}")
        f.close()
        messagebox.showinfo(title="Add Successfull")


    def Display(self):
        a4=e4.get()
        f=open("love.txt","r")
        for i in f:
            if a4 in i:
                print(i)
                l5=Label(win,text=i)
                l5.grid(row=7,column=1)
        f.close()
        messagebox.showinfo(title="Display successful")
        
    def Delete(self):
        a5=e6.get()
        f=open("love.txt","r")
        res=f.readlines()
        f.close()
        for i in res:
            if a5 in i:
                res.remove(i)
                messagebox.showinfo(title="Delete successful")
        f=open("love.txt","w")
        for i in res:
           f.write(i) 
        f.close()
    
    def search(self):
        pass 
    
    def clear():
        pass

m=MobileStore()

win=Tk()
win.geometry("600x600")
win.config(bg="Red")
win.title("MobileStore")
l=Label(win,text="Mobile_Store")
l.grid(row=0,column=3)
l1=Label(win,text="MobileName")
l1.grid(row=1,column=0)
l2=Label(win,text="MobileBrand")
l2.grid(row=2,column=0)
l3=Label(win,text="MobilePrice")
l3.grid(row=3,column=0)
e1=Entry(win)
e1.grid(row=1,column=1)
e2=Entry(win)
e2.grid(row=2,column=1)
e3=Entry(win)
e3.grid(row=3,column=1)
l4=Label(win,text="MobileName")
l4.grid(row=5,column=0)
e4=Entry(win)
e4.grid(row=5,column=1)
l6=Label(win,text="MobileName")
l6.grid(row=8,column=0)
e6=Entry(win)
e6.grid(row=8,column=1)
b1=Button(win,text="Save",command=m.Add)
b1.grid(row=4,column=1)

b2=Button(win,text="Display",command=m.Display)
b2.grid(row=6,column=1)
b3=Button(win,text="Delete",command=m.Delete)
b3.grid(row=9,column=1)
b4=Button(win,text="Exit",command=quit)
b4.grid(row=11,column=1)

win.mainloop()



        

