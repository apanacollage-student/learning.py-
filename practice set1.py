import pyttsx3
engine=pyttsx3.init()
engine.say("this chapter is about back revision.")
engine.runAndWait()



a=10
b=float(a) #type casting
t=type(b)
print(t)
#type function is used to check the type of variable

#arthmetic operation
a=10
b=50
c=a*b
print(c)

#assignment operator
d=100
d*=4
print(d)

#comprision operator
a=10>5
print(a)

b=5!=6
print(b)

c=5==6
print(c)

#logical operator
#and or not
print("True or False is", True or False)
print("False or True is", False or True)

#and 
print("True and False is", True and False)
print("True and True is", True and True)

# not operator jo true ko false and false to true kar deta hai
print("not True is", not True)
print(not(False))
print(not(5>6))
# type conversion
a=int(input("enter number1:"))
b=int(input("enter number2:"))
print("number 1 is",a)
print("number 2 is",b)
print("the sum is",a+b)

#find the remainder
a=35
b=5
c=a%b
print("remainder is", c)

# a is grater than b
a=int(input("enter number1:"))
b=int(input("enter number2:"))
print("a is greater than b is :", a>b)

# find the average of two numbers
a=int(input("enter number1:"))
b=int(input("enter number2:"))
print("average of two number is:", (a+b)/2)

# find the square of a number
a=int(input("enter number1:"))
print("square of a number is:",a*a)

