# teeno condition in condition
a=int(input("enter your age:"))
if(a>=18):
    print("your age is good")
    print("and good for you")

elif(a<0):
    print("you enter a not valid age")
    print("please enter valid age")


else:
    print("your age is under 18:")



#check the odd and even number for condition
a=int(input("enter your number"))
if(a%2==0):
    print("this number is even")

else:
   print ("this is not even number")


b=int(input("enter your number:"))
if(b%2!=0):
    print("this is odd number")

else:
    print("this is even number not a odd")


    #this is a loop and condition
    list=[]
for i in range(0,20):
    Value=int(input("enter your number:"))
     
   

list.append(Value),

if(i%2!=0):
    print("this is a odd number", )
print(list,i)


#   CHAPTER 6 PRACTICE SET

#QUESTION ONE 

         #WRITE A PROGRAM TO FIND THE GRATEST OF FOUR NUMBER ENTERED 
         #BY USER
a=int(input("enter your numberA:"))
b=int(input("enter your numberb:"))
c=int(input("enter your numberc:"))
d=int(input("enter your number:"))

if(a>b and a>c and a>d):
    print("the   grater number is A",a)
elif(b>a and b>c and b>d):
    print("the  grater number is b",b)
elif(c>a and c>b and c>d):
    print("this  gratest number is c",c)
elif(d>a and d>b and d>c):
    print("this grater number is d")






 # write a program find out a 3 student has passed or failed and 
# it require 40% and each subject 30% and input from the user

      # question 2[marksheet]

marks1=int(input("enter your marks1:"))
marks2=int(input("enter your marks2:"))
marks3=int(input("enter your marks3:"))

marks_percentage=(100*(marks1+marks2+marks3))/300

if(marks_percentage>=40 and marks1>=30 and marks2>=30 and marks3>=30):
    print("you are passed",marks_percentage)

else:
    print("you are failed,try again next time and padh le bsdk",marks_percentage)





#       QUESTION 3

   # WRITE SPAM COMMENT IS DEFINED AS A TEXT CONTANING WORD 
    #"MAKE A LOT OF MONEY"
    # "GANDU"
    #"BSDK"
    # "CLICK THIS"

p1="make a lot of money"
p2="gandu"
p3="bsdk"
p4="click this"

massage=input("enter your massage:")

if(p1 in massage or p2 in massage or p3 in massage or p4 in massage):
    print("this comment is a spam")


else:
    print("this comment is not spam ")
    print("this is good")




         # yaaa

pa="massage"
pb="kaanu"
pc="  "
pd="kuch v"

massage=input("enter your massage:")

if(pa and pb and pc and pd):
    print("this is spam")

else:
    print("this is not spam")






    # 4 question

   # write a program to find wether a give username contains less than
      # 10 characters

username=input("enter your username:")

if(len(username)<10):
    print("your name is less than 10 charater")

else:
    print("your name is right of necerscery")






          # WRITE A PROGRAM WHICH FIND OUT A GIVEN NAME PRESENT IS A LIST
     
         # QUESTION NUMBER 5
lis=[ "ayush","komal"]

name=input("enter your list name:")

if(name in lis):
    print("this name is avilable in list")

else:
    print("this name is not avilable in list")




    
  # write a program to calculatye grade of a student for depend on his marks
     # flowing scheme

       #100-90=ex
      #90-80=A
    # 80-70=b
    # 70-60=c
    #60-50=e
   # 50=f
       

     # question number 6
marks=int(input("enter your marks to get grade:"))

if(marks<100 and marks>=90):
     grade="ex"
elif(marks<90 and marks>=80):
    grade="good"
elif(marks<80 and marks>=70):
    grade="A"
elif(marks<70 and marks>=60):
    grade="B"
elif(marks<60 and marks>=50):
    grade="C"
elif(marks<=50):
    grade="D"

print("your grade is",grade)






   # post talking about ayush yes ya no 

name=input("enter about you:")

if("ayush" in name.lower()):
    print("this post about ayush")

else:
    print("this post not about ayush")



