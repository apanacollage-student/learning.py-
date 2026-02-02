#FUNCTION KISI V AKE CODE KO MULTIPLE TIME PRINT KARNA HO TO
#ex
# a=14
# b=488
# c=44
# avg=(100*(a+b+c))/3
# print(avg)# ye baar baar code na likhna pare
# 
          ########function#########
def avg():
    a=int(input("enter your number:"))
    b=int(input("enter your number:"))
    c=int(input("enter your number:"))
    avg1=(a+b+c)/3
    print(avg1)
avg()
print("this is your result thanku")



#how to use a function
#!1.....
def avg():
    a=int(input("enter number1:"))
    b=int(input("enter number2:"))
    c=int(input("enter number3:"))
    avg=100*(a+b+c)/3
    print(avg)
avg()
avg()
avg()
avg()
avg()
avg()
avg()

# function with argumernt
def goodday(name,ending):
    print("goodday ", name)
    print(ending)
    return "ok"
a=goodday("ayush","yadav")
print(a)

# function with table 
def table():
    table=int(input("enter your table:"))
    for i in range(0,11):
        print(f"{table}*{i}={table*i}")
table()
print("thanks:aryan")
table()
print("thanks:aryan")
table()
print("thanks:aryan")
table()
print("thanks:aryan")
table()
print("thanks:aryan")
table()
print("thanks:aryan")
table()
print("thanks:aryan")

# function with argumernt
def goodday(name,ending):
    print("goodday ", name)
    print(ending)
    return "ok"
a=goodday("ayush","yadav")
print(a)

#defult parameter value in function
def goodDay(name,ending="thanku boss"):
    print("good day",name)
    print(ending)
goodDay("ayush")
goodDay("aniket","yadav")



#defult value in   function\\\\
def goodd(name,ending="thanks"):
    print("good",name)
    print(ending)
    
goodd("ayush")
goodd("aniket","yadav")

# factorial
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
a=int(input("enter your number:"))
print("the factorial of number is:",factorial(a))

######print a new line in python###########

print("ayush")
print(500)
print("one-hundred:",end="")
print(100,end="")



