name='ayush' # string sclicing
nameshort=name[0:3]
print(nameshort)

# spacfic character print
name="ayush"
character=name[1]
print(character)
 
 # nagative string
name='ayush'
print(name[-4:-1])

# character ka lenth
name='ayush'
print(len(name))

#character endwith
name='ayush'
print(name.endswith("s"))

#small latter ko capital me change karna
name='ayush'
print(name.capitalize() )

#replace character
a='ayush'
print (a.replace("ayush","yadav"))

#find character ki kitna number pe hai
a='ayush yadav'
print(a.find("yadav"))

#practice set chapter3
#write a python program to display a user entered name followed by goodafternoon using input
name=input("enter your name:")
print(f"good after noon {name}")

# write a program to fill in a latter template given bellow with name and data
latter='''dear <|name|>,
      you are selected 
                   <|date|>'''
print(latter.replace("<|name|>","ayush").replace("<|date|>","28 january 2025"))

#write a program to detect double space in a string
name="ayush is a good   boy"
print(name.find("good"))

# write program to format the flowing latter using escape sequence character
latter="dear ayush, \n \t this is your practice set"
print(latter) 

#command me koi chij add karna
friends=["apple,""banana"]
friends.append("ayush") # add
print(friends)

# number short karna yani number me arrang karna                                          
a=[1,34,12,2,5,3]
# a.sort() # serial number me laane ke lea
# a.reverse() reversed karne ke lea number
#a.remove(34) #remove karne ke lea
#a.pop(3) 3rd position pe hai so deleate karne ke lea
value=a.pop(3) #return of value jo deleate hua tha
print(value)
a=(1,) #type of tupple data
print(type(a))

a=(1,45,45,46) #count ki ake data kitne baar diya hai
no=a.count(45)
print(no)

#position check karne ke lea 
b=[1,6,6,5,4]
i=b.index(6)
print(i)


#lenth check
c=[1,3,6,6,6,5]
i=(len(c))
print(i)

# 1 write a progrm to store seven fruits in a list entered by the user
fruits=[]
f1=input("enter fruits name1:")
fruits.append(f1)
#append kisi chij ko add karne ke lea 
f2=input("enter fruits name2:")
fruits.append(f2)

f3=input("enter fruits name3:")
fruits.append(f3)

f4=input("enter fruits name4:")
fruits.append(f4)

f5=input("enter fruits name5:")
fruits.append(f5)

f6=input("enter fruits name6:")
fruits.append(f6)

f7=input("enter fruits name7:")
fruits.append(f7)

print(fruits)

# 2 write a program to accept marks of 6 student and display them in stored manner code
marks=[]
f1=int(input("enter mark here1:"))
marks.append(f1)

f2=int(input("enter mark here1:"))
marks.append(f2)


f3=int(input("enter mark here1:"))
marks.append(f3)


f4=int(input("enter mark here1:"))
marks.append(f4)


f5=int(input("enter mark here1:"))
marks.append(f5)


f6=int(input("enter mark here1:"))
marks.append(f6)

print(marks)

# 3 check that a tupels type cabbot be changed in python
#a=(34,234,"ayush")
#a[2]="yush"
#print(a)  #ye change nahi ho ga error aaye ga 


# 4 write a program to sum a list with 4 number
l=[34,35,36,37]
print(sum(l))

# 5 write a program to count the number of zero in following tuple a=(7,0,8,0,0,9)
a=(7,0,8,0,0,9)
n=a.count(0)
print(a)




# list are are store multiple values and datatypes
name=["ayush","ram","shyam","hari","gita",34,56.7,True]

#change in data is possible
name[0]="aniklet"

# any data add kar sakte ho
name.append("new name added")

print(name)

# sort kar sakte ho
n=[34,67,89,23,12,45]
n.sort()
print(n)

# new item add kar sakte ho               
print(n)

# remove kar sakte ho   
n.remove(45)
print(n)

# remove return kar sakte ho
print(n.pop())




# tuple are also store multiple values and datatypes
# but change in data is not possible imutable data type``
name=("ayush","ram","shyam","hari","gita",34,56.7,True)
print(name)

a=(1,)
print(type(a)) #type of tupple

# count of item in tupple
a=(1,2,3,4,5,1,2,1,1)
b=a.count(1)
print(b)

# index of item in tupple possition of data 
c=a.index(5)
print(c)

# length of tupple
d=len(a)
print(d)

#name and fevorite fruits store karne ke lea
list=[]
for i in range(0,8):
    name=input("enter the name:")
    list.append(name)
    fruits=input("enter your fevorite fruits:")
    list.append(fruits)
    print(list)
# student marks store karne ke lea
list=[]
for i in range(0,8):
        name=input("enter your name:")
        list.append(name)
        roll=int(input("enter your roll number:"))
        list.append(roll)
        marks=int(input("enter your marks:"))
        list.append(marks)
        print(list)


# dictionary are store data in key value pair

dict={
    "name":"ayush-yadav",	
    "age":19,
    "collage":"iibm,patna",
    "city you currently live in":"patna"

}
print(dict.get("aniklet")) #if key is not present then it will return none      
print(dict.items()) #return key value pair in tuple formate
print(dict.keys()) #return all keys in dictionary
print(dict.values()) #return all values in dictionary

print(dict)


# set are store multiple values but unorderd and unindexed

a = set([1,1,2,2,3,]) # set me same value ek hi bar store hoti hai
print(a)
b = set([1,2,3,4,5,5,5])
print(b.add(6)) # add set me value add karne ke lea hota hai
print(b)
b.remove(3) # remove set me se value remove karne ke lea hota hai
print(b)
b.discard(4) # discard bhi remove karne ke lea hota hai
print(b)
b.clear() # clear set ko khali karne ke lea hota hai
print(b)
b.pop() # pop set me se random value remove karne ke lea hota hai
print(b)


#short wey to practice set

set=set([1,2,3,4,5,5,5])
print(type(set))
set.add(100)
print(set)
set.pop()
print(set)
set.remove(3)
print(set)
set.clear()
print(set)

#dictionary
word={
    "aam":"mango",
    "kela":"banana",
     "ray":"yadav",
     "hara": "green",
    "zindagi": "life",
    "mohabbat": "love",

}
word_input = input("welcome ayush hindi and english dictionary:",)
print("the meaning of your word is:", word.get(word_input, "word not procesing in dictionary"))

#set unique number
s=set()
for i in range (0,9):
    a=int(input("enter your number:"))
    s.add(a)
    print("enter your unique number is :",s)




    # we can set 2 value int and str
s=set()
s.add(18)
s.add("18")
print(s)



# what will be lenth of these number
s=set()
s.add(20)
s.add(20.0) # output 2 becouse 20 and 20.0 is same values
s.add("20")
print(len(s))


#create the name and fav language
dit={}
for i in range(0,5):
    name=input("enter your name:")
    lang=input("enter your fav coding language:")
    dit.update({name:lang})
    print("your fav language is this:",dit)


    #condition method
    a=int(input("enter your age:"))
if(a>=18):
    print("your age is good")
    print("and good for you")

else:
    print("your age is under 18:")


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



#CHAPTER 6 PRACTICE SET Q1
a=int(input("enter your numberA:"));
b=int(input("enter your numberb:"));
c=int(input("enter your numberc:"));
d=int(input("enter your number:"));

if(a>b and a>c and a>d):
    print("the   grater number is A",a);
elif(b>a and b>c and b>d):
    print("the  grater number is b",b);
elif(c>a and c>b and c>d):
    print("this  gratest number is c",c);
elif(d>a and d>b and d>c):
    print("this grater number is d")



# question my mind user enter name and rool and get marks
name1="ayush"
roll1=15
marks1=95

name2="kumar"
roll2=12
marks2=45

name=input("enter your name:")
roll=int(input("emter your roll:"))

if(name==name1 and roll==roll1):
    print("your marks",marks1)

elif(name==name2 and roll==roll2):
    print("your marks",marks2)

else:
    print("data not pound")


 #write a program to calculate the grade of a student from his marks from the flowwing scheme

marks=int(input("enter your marks:"))
if(marks<100 and marks>90):
    grade="excelent"
    print("your grade is:",grade)
elif(marks<90 and marks>80):
    grade="a"
    print("your grade is:",grade)
elif(marks<80 and marks>70):
    grade="b"
    print("your grade is:",grade)
    
#7 WRITE A PROGRAM TO FIND OUT WHETHER A GIVEN PAST TALKING ABOUT "ME"
me="ayush"
name=input("enter about me:")

if("ayush" in me.lower()):
    print("this this all about me")

