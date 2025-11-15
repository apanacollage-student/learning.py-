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
 
# write a program to store seven fruits in a list entered by the user
fruits=[]
for i in range(1,8):
    fruit=input("enter the name of fruit:")
    fruits.append(fruit)
print(fruits)


#type of tupple
a=(7,0,8,0,0,9)
a[5]
n=type(a,)

print(n)


#sum of list 4 numbers
numbers=[10,2,3,4]
sum=0
for i in numbers:
    sum=sum+i
print(sum)

# count the number of zero in following tuple``
a=(7,0,8,0,0,9)
b=a.count(0)
print(b)



