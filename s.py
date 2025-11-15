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
 
