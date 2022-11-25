
import random
import json

class Employee():
    employee = []
    def createID(self,name,skill):
        self.__dict = {}
        self.__dict["id"] = "CN"+str(random.randint(1000,9999))
        self.__dict["name"] = name 
        self.__dict["skill"] = skill 

        Employee.employee.append(self.__dict)

        with open ("employee.json","w") as f:
            json.dump(Employee.employee,f)

    def update(self ,id, name = "none", skill = "none"):
        try:
            with open("employee.json","r") as f:
                res = json.load(f)
                print(res)
        except FileNotFoundError:
            print("File not found")

        for i in res:
            if i["id"] == id:
                data = i 
                # print(data)
                if name == "none":
                    data["skill"] = skill
                elif skill == "none":
                    data["name"] = name 
                else:
                    data["name"] = name 
                    data["skill"] = skill
            else:
                print("id not found")
        
        with open("employee.json","w") as f:
            json.dump(res,f)
        
    def read(self,id):
        try:
            with open("employee.json","r") as f:
                res = json.load(f)

        except FileNotFoundError as e:
            print("File not found")
            exit()
        
        for i in res:
            if i["id"] == id:
                print(i)
            else:
                print("id not found")

    def realAll(self):
        try:
            with open("employee.json","r") as f:
                res = json.load(f)
        except FileNotFoundError as e:
            print("File not found")
            exit()

        print(res)

    def delete(self,id):
        try:
            with open("employee.json","r") as f:
                res = json.load(f)
        except FileNotFoundError as e:
            print("File not found")
            exit()
        for i,v in enumerate(res):
            if v["id"] == id:
                del res[i]
            else:
                print("id not found")
        
        with open("employee.json","w") as f:
            json.dump(res,f)

emp = Employee()


while(True):
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    choice = int(input(""))

    if choice == 1:
        name = input("Name: ")
        skill = input("Skill: ")
        emp.createID(name,skill)

    if choice == 2:
        c = input("Read specific employee Y/N:  ")
        if c.lower() == "y":
            id = input("ID: ")
            emp.read(id)
        else:
            emp.realAll()

    if choice == 3:
        id = input("ID: ")
        name = input("Name: ")
        skill = input("Skill: ")
        if name == "":
            print("name not given")
            emp.update(id,name=name)
        elif skill == "":
            print("skill not given")
            emp.update(id,skill=skill)
        else:
            emp.update(id,name,skill)
        

    if choice == 4:
        id = input("ID: ")
        emp.delete(id)
        