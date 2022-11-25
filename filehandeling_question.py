import os

def creating():
    global name
    name = input("Enter name of file: ")
    print(name)
    with open(name,"w") as f:
        pass
def updating():
    global name
    if not name:
        name = input("Enter name of file: ")
        with open(name,"a") as f:
            f.write(input("Enter content: "))
    else:
        print("1.Use Same File Name")
        print("2.Use DIfferent File Name")
        k = int(input())
        if k == 1: 
            with open(name,"a") as f:
                f.write(input("Enter content: "))
        elif k == 2 :
            name = input("Enter name of file: ")
            with open(name,"a") as f:
                f.write(input("Enter content: "))
        else:
            raise Exception
def read():
    global name
    if not name:
        name = input("Enter name of file: ")
        with open(name,"r") as f:
            print(f.read())
    else:
        print("1.Use Same File Name")
        print("2.Use DIfferent File Name")
        k = int(input())
        if k == 1 :
            with open(name,"r") as f:
                print("->",f.read())
        elif k == 2 :
            name = input("Enter name of file: ")
            with open(name,"r") as f:
                print("->",f.read())
        else:
            raise Exception
def delete():
    if not name:
        n = input("Enter name of file: ")
        os.remove(n)
    else:
        print("1.Use Same File Name")
        print("2.Use DIfferent File Name")
        k = int(input())
        if k == 1 :
            os.remove(name)
        elif k == 2 :
            n = input("Enter name of file: ")
            os.remove(n)
        else:
            raise Exception

try:
    name = ""
    i = 0
    while i != 5:
        print("\n------WELCOME TO FILE HANDLER-----")
        print("1. For Creating The File")
        print("2. For Updating The File")
        print("3. For Reading The File")
        print("4. For Deleting The File")
        print("5. Exit")
        thing = int(input())
        if thing == 1:
            creating()
        elif thing == 2:
            updating()
        elif thing == 3:
            read()
        elif thing == 4:
            delete()
        elif thing == 5:
            print("Visit Again")
            exit(1)
        else:
            print("Enter Valid Option...!!!")


except FileNotFoundError:
    print("File Not Found....!!!")
except Exception:
    print("Please Enter Details properly...!!!")