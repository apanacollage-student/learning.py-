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
n.insert(2,100)
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









