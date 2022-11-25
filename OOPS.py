#-----------Circle---------------------
# class Circle:
#     def __init__(self,r):
#         self.__radius = r

#     def area(self):
#         return (self.__radius**2)*3.14
    
#     def circumference(self):
#         return 2*3.14*self.__radius
    
# c = Circle(9)
# print(c.area())
# print(c.circumference())

#----------------Student---------------
# class Student:
#     details = {}
#     def __init__(self,name):
#         self.__name = name
#         Student.details[name] = {}

#     def add_age(self,age):
#         Student.details[self.__name]["age"] = age 
    
#     def add_marks(self,marks):
#         Student.details[self.__name]["marks"] = marks 

#     def display(self):
#         print(Student.details)

# std = Student("anurag")
# std.add_age(19)
# std.add_marks(96)
# std.display()

#-----------------time-------------------
# class Time:
#     __samai = ""
#     __min = ""
#     def __init__(self,l):
#         t = l[0]*60
#         t += l[1]
#         self.__time = t
#     def __add__(self,other):
#         l = self.__time + other.__time
#         hh = l//60
#         mm = l-(hh*60)
#         Time.__min = mm
#         Time.__samai = f"{hh}h {mm}m"
#     def Print():
#         print(f"{Time.__samai}")

#     def PrintMin():
#         print(f"{Time.__min}m")
# time1 = Time(list(map(int,input().split())))
# time2 = Time(list(map(int,input().split())))
# time1 + time2
# Time.Print()
# Time.PrintMin()

#-----------------Property------------------
# class Profile:
#     def __init__(self):
#         self.__age = 0
#     def set(self,n):
#         self.__age = n
#     def get(self):
#         return self.__age
#     age = property(get,set)

# mark = Profile()
# mark.age = 9
# print(mark.age)

#---------------email--------------------
class Profile:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,mail):
        name = mail.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    def show(self):
        return f"Name: {self.fname} {self.lname}\nEmail: {self.fname}.{self.lname}@gmail.com"


person = Profile("anurag","sarkar")
print(person.show())
person.email = "gaurav.solanki@gmail.com"
print(person.show())

#---------------------



