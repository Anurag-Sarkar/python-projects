from cryptography.fernet import Fernet
import csv

# key = Fernet.generate_key()
# with open("key.key" , "wb") as key_file:
#     key_file.write(key)
try:
    class Encrypt:

        def __init__(self,master):
            self.__main = "password"
            with open("key.key","rb") as k:
                self.__k = k.readline()

            if self.__k+self.__main.encode() == self.__k+master.encode():
                self.__key = self.__k + self.__main.encode()
            else: 
                print("No")
                exit()

        def encrypt(self,name,password): 
            state = True   
            with open("csv.csv","r") as c:
                read = csv.reader(c)
                for row in read:
                    if len(row) > 0:
                        if row[0] == name:
                            state = False
                        else:
                            state = True
            if state:
                f = Fernet(self.__key)
                token = f.encrypt(password.encode())
                row = [name,token.decode()]
                with open("csv.csv","a") as c:
                    writer = csv.writer(c)
                    writer.writerow(row)
            else:
                print("Name already exists!")  


        def decrypt(self,name):
            with open("csv.csv","r") as c:
                read = csv.reader(c)
                for row in read:
                    if len(row) > 0:
                        if row[0] == name:
                            n = row[1]
                            f = Fernet(self.__key)
                            return f.decrypt(n.encode()).decode() 
                        else:
                            ("Name Not Found" )
        
        def show_all(self):
            with open("csv.csv","r") as c:
                read = csv.reader(c)
                for row in read:
                    if len(row) > 0:
                        f = Fernet(self.__key)
                        print(row[0],f.decrypt(row[1].encode()).decode())

    
    m = input("Master Password: ")
    enc = Encrypt(m)
    choice = 0
    while choice != 5:
        print("1. To add password")
        print("2. To see password")
        print("3. View all Passwords")
        print("4. To exit")
        choice = int(input())
        if choice == 1:
            name = input("Enter Name: ")
            pas = input("Enter password: ")
            enc.encrypt(name,pas)
        if choice == 2:
            name = input("Enter Name: ")
            print(enc.decrypt(name))
        if choice == 3:
            enc.show_all()
        if choice == 4:
            exit()

except AttributeError as e:
    print("Enter correct passcode")

