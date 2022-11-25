import csv
class Rental:
    stock = 0
    def __init__(self):
        self.__stock = 0

    def view_stock(self):
        print("Current Stock: ",Rental.stock)
        with open ("./rent.csv" , "r") as r:
            reader = csv.reader(r)
            for row in reader:
                if len(row) > 1:
                    if row[1] == "5":
                        print(row[2],"Bike will be returned in",row[3],"hrs")
                    if row[1] == "50":
                        print(row[2],"Bike will be returned in",row[3],"days")
                    if row[1] == "150":
                        print(row[2],"Bike will be returned in",row[3],"weeks")
        
    def stock(self):
        if self.__stock <= 0:
            Rental.stock = int(input("Enter new stock: "))
                            
        elif self.__stock > 0:
                print("Current Stock: ",self.__stock)
                c = input("Do you want to restock? (yes/no): ")
                if c == "yes":
                    restock = int(input("Enter new stock: "))
                    Rental.stock = Rental.stock + restock
                else:
                    pass

    def rent(self,type,name,bikes,duration):
        with open("./rent.csv","r") as r:
            reader = csv.reader(r)
            for row in reader:
                if len(row) > 0:
                    if row[0] == name:
                        print("Customer already availed service")
                    else:    
                        self.__type = type
                        self.__name = name
                        self.__bikes = bikes
                        self.__duration = duration
                        cost = self.__type*duration*bikes
        row = [self.__name,self.__type,self.__bikes,self.__duration,cost]
        with open ("./rent.csv","a") as r:
            writer = csv.writer(r)
            writer.writerow(row)

    def bill(self,name):
        with open("./rent.csv","r") as r:
            reader = csv.reader(r)
            for row in reader:
                if len(row) > 0:
                    if row[0] == name:
                        print("\n----Thanx for using our service----")
                        print("Name: ",row[0])
                        print("Bikes rented: ",row[2])
                        if row[1] == "5":
                            print("Type: Hour @ $5")
                        if row[1] == "50":
                            print("Type: Day @ $50")
                        if row[1] == "150":
                            print("Type: Week @ $150")
                        print("Amount: ",row[4])
                        print("----Visit Again----")
                    else:
                        print("Name not Found")
rent = Rental()