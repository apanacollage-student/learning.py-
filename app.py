
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

    