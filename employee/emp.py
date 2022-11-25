import json
from pathlib import Path

class Employee:
    employee = []
    if not Path("employ.json").exists():
        with open("employ.json","w") as file:
            file.write(json.dumps([]))
    with open("employee.json","r") as file:
        emp = json.load(file)
    # print(emp)
    def __str__(self):
        return "lawde 80,0000 shiwzz hai "
    
    @classmethod
    def countEmploye(cls):
        with open("employee.json","r") as file:
            e = json.load(file)
            print(len(e))

employ = Employee()
print(employ)
employ.countEmploye()