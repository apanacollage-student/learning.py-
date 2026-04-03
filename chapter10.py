#instance of class
class employee:
    language="python"
    salary=12000

ayush=employee()
print(f"salary:{ayush.salary},language:{ayush.language} ",)


#self method
class employee:
    language="python"
    salary=2500000
    name="ayush"
    #@staticmethod =ye use karne se self nahi dena parta hain
    def getinfo(self):
        print(f"the name is:{self.name}\nthe language is:\n{self.language}.the salary is:\n{self.salary}")
    def greet(self):
        print("good morning",self.name)
ayush=employee()
ayush.getinfo()
ayush.greet()


#__init__() constructor
class employee:
    @staticmethod
    def greet():
        print("welcome the ayush company to get your info",)


    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

    def getinfo(self):
        print(f" name is:{self.name}\n salary is:{self.salary}\n language is:{self.language}")

ayush=employee("ayush",500000,"java")
employee.greet()
ayush.getinfo()

rahul=employee("rahul",125000,"python")
employee.greet()
rahul.getinfo()

print("yarly salary ayush:",ayush.salary*12)
print("yarly salary rahul",rahul.salary*12)

if ayush.salary>rahul.salary:
    print(ayush.name,"more salary")

else:
    print(rahul.name,"more salary")

    