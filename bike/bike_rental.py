import csv

from Bike import rent 
try:
    choice = 1
    while int(choice) != 0:
        print('''
        1. To rent bike on Hour basis ($5)
        2. To rent bike on Day basis ($50)
        3. To rent bike on Week basis ($150)
        4. To view stock
        5. To Generate bill'''
        )
        choice = int(input())
        if choice == 1:
            name,bikes,time = input("Enter details as Name,Bikes,Hours: ").split()
            rent.rent(5,name,int(bikes),int(time))
        elif choice == 2:
            name,bikes,time = input("Enter details as Name,Bikes,Days: ").split()
            rent.rent(50,name,int(bikes),int(time))
        elif choice == 3: 
            name,bikes,time = input("Enter details as Name,Bikes,Week: ").split()
            rent.rent(150,name,int(bikes),int(time))
        elif choice == 4: 
            rent.view_stock()
        elif choice == 5:
                name = input("Enter Name: ") 
                rent.bill(name)
        elif choice == 6:
                rent.stock()
        else: 
            print("Incorrect option!!!")

except ValueError as e:
    print("Enter values correctly!")
except FileNotFoundError as e:
    print("File not Found. \nPlease wait till we fix it...!")
    with open ("rent.csv","a") as r:
        pass