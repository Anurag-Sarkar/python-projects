#create
#read/all
#update
#delete
#json

import json
import random
from pathlib import Path


class Employee:
    employee = []
    if not Path("employee.json").exists():
        with open("employee.json","w") as file:
            file.write(json.dumps([]))
    
    with open("employee.json","r") as file:
            employee = (json.load(file))

    __count = 0

    def __str__(self):
        return "lawde 80,000 ke shoezz hain, tera ghar chle jaenge isme..."

    @classmethod
    def countEmployee(cls):
         with open("employee.json","r") as file:
            employee = (json.load(file))
            print(len(employee))
            
    def create(self):
        
        self.__dict = {}
        self.__dict["id"] = "SHERY" + str(random.randint(1000,9999))
        self.__dict["name"] =  input("Enter name: ")
        self.__dict["skill"] = input("Enter Skill: ")

        Employee.employee.append(self.__dict)

        with open("employee.json","w") as file:
            json.dump(Employee.employee,file)
    
    def read(self):
        id = input("Enter ID to search: ")
        with open("employee.json","r") as file:
            data = (json.load(file))
        for i in data:
            if i["id"] == id:
                print()
                print(f'ID: {i["id"]}')
                print(f'Name: {i["name"]}')
                print(f'Skill: {i["skill"]}')
                print()
                break
            
        else:
            print("ID not found")

    def readAll(self):
        with open("employee.json","r") as file:
            data = (json.load(file))
        if data:
            print(data)
        else:
            print("no data")

    def update(self):
        id = input("Enter ID to search: ")
        with open("employee.json","r") as file:
            data = (json.load(file))
        for i in data:
            if i["id"] == id:
                name = input("Enter new name: ")
                if name:
                    i["name"] = name
                skill = input("Enter new name: ")
                if skill:
                    i["skill"] = skill
                    break
                else:
                    print("details to de lawde")
                    break
        else:
            print("ID not found")
        with open("employee.json","w") as file:
            json.dump(data,file)


    def delete(self):
        id = input("Enter ID to search: ")
        with open("employee.json","r") as file:
            data = (json.load(file))
        for i,v in enumerate(data):
            if v["id"] == id:
                print(i)
                del data[i]
        else:
            print("ID not found")
        with open("employee.json","w") as file:
            json.dump(data,file)


emp = Employee()

# while True:
#     print("1. Create")
#     print("2. Read")
#     print("3. Update")
#     print("4. Delete")
#     choice = (input())
#     if (choice) == "1":
#         emp.create()
#     if (choice) == "2":
#         emp.read()
#     if (choice) == "3":
#         emp.update()
#     if (choice) == "4":
#         emp.delete()
#     if choice == "readall":
#         emp.readAll()
#     if choice == "count":
#         emp.countEmployee()
print(emp)