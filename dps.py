#defining class
class Sustain():

    #defining constructor
    def __init__(self):
        self.__pwsd = "dpsbhopal"
        print ("\nHello welcome to Sustainable Devlopment program!\n")
        
    #making a method to validate password and register name
    def Authorise(self):
        self.__name = input("Enter Name: ")
        self.__password = input("Enter Password: ")
        if self.__password != self.__pwsd:    
            print("Password Mismatch")
            exit()   
    # exits the code if password doesnt match 

    #making "No Poverty" Method 
    def poverty(self):
        print('''\nEradicating poverty is not a task of charity, it’s an act of justice and the key to unlocking an enormous
human potential. Still, nearly half of the world’s population lives in poverty, and lack of food and clean water is
killing thousands every single day of the year. Together, we can feed the hungry, wipe out disease and give everyone
in the world a chance to prosper and live a productive and rich life.''')
        print("\nFollowing are the ways to do it")
        print("1. Find a Goal 1 charity you want to support. Any donation, big or small, can make a difference!")
        print("2. Donate what you don’t use. Local charities will give your gently used clothes, books and furniture a new life.")
        print("3. Support campaigns collecting items for victims of emergencies. Donate your clothes, food supplies etc. to support those in need.")
        print("\nQUESTION")

        #asking Question
        ans = int(input('''By which year, we need to eradicate Extreme Poverty for all people everywhere, currntly measured
as people living on less than Rs 100 per day?\n'''))
        #checking Answer
        if ans == 2030:
            print(f"Congratulation {self.__name} you have passed the test\n")
        else:
            print(f"Better luck next time\n")
    
    #making "Quality Education" Method
    def education(self):
        print('''\nEducation is one of the fundamental rights of every citizen in most countries. Education plays a significant 
role in the overall development of the child. Education and Literacy shape the future of the country.
        
Unfortunately, millions of children across the world are deprived of their right to education for various reasons. 
Especially children in under-developed countries have a lower education rate. United Nation’s 4th SDG is to make 
quality education accessible to all despite all the differences.''')
        print("\nFollowing are the ways to do it")
        print("1. Advocate and Spread Awareness")
        print("2. Train Teachers")
        print("3. Talk to the Parents")
        print("\nQUESTION")

        #asking Question
        ans = input('''Before which crisis, projection showed that more than 200 million children would be out of school?\n''')
        #checking Answer
        if ans.lower() == "coronavirus":
            print(f"Congratulation {self.__name} you have passed the test\n")
        else:
            print(f"Better luck next time\n")
    
    #making "Quality Education" Method
    def inovation(self):
        print('''\nA functioning and resilient infrastructure is the foundation of every successful community. To meet future 
challenges, our industries and infrastructure must be upgraded. For this, we need to promote innovative sustainable 
technologies and ensure equal and universal access to information and financial markets. This will bring prosperity, 
create jobs and make sure that we build stable and prosperous societies across the globe.''')
        print("\nFollowing are the ways to do it")
        print("1. Develop sustainable, resilient and inclusive infrastructures")
        print("2. Increase Access to financial services and markets")
        print("3. Upgrade all industries and infrastructure for sustainablity")
        print("\nQUESTION")

        #asking Question
        ans = input('''6 in 10 people today use which Techonology?\n''')
        #checking Answer
        if ans.lower() == "internet":
            print(f"Congratulation {self.__name} you have passed the test\n")
        else:
            print(f"Better luck next time\n")

run = Sustain()
run.Authorise()
print("\nIMPORTANT GOALS OF SUSTAINABLE DEVELOPMENT")
while True:
    #running loop continously to accept responses
    print("1. No Poverty")
    print("2. Quality Education")
    print("3. Industry, Infrastructure and Innovation")
    print("exit")
    c = input()
    if c == "1":
        run.poverty()
    if c == "2":
        run.education()
    if c == "3":
        run.inovation()
    if c == "exit":
        print("Thank You")
        break
    #type "exit" to exit the code
    else:
        print("Enter Correct Choice!!!")