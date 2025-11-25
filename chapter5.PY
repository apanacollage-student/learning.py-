# dictionry is a collection which is unordered, changeable and indexed.
#  In Python dictionaries are written with curly brackets, and they have keys and values.

marks={
    "ayush":35,
    "ram":45,   
    "shyam":55,
    "hari":65,
    "gita":75,

}
print(marks)
print(type(marks))

# items value  ake box me store kar sakte ho keys and values separately
print(marks.items())

# can be store only keys values separately
print(marks.keys())


# can be store only values separately
print(marks.values())

#can a values and keys are update and add more keys values 
marks.update({"ayush":100})
marks.update({"aman":355})  # ADD MORE KEY VALUES
print(marks)


# get method use kar ke value ko access kar sakte ho
print(marks.get("ram")) # ram ka value add ho jaaye ga 
print(marks.get("saurabh"))  # ye none return kare ga becouse saurabh key dictionry me nahi hai






#    SETS IN PYTHON
# SETS ARE COLLECTION OF NON-ORDERED AND UNINDEXED ITEMS

# CREATEB A EMPTY SET
a=set()
print(type(a))

# create a empty dictionary
b={}
print(type(b))


# create a sets with values
a={1,2,3,4,4,5,5,6,7,8,8}
print(a)  # duplicate values are not allowed in sets 
print(len(a)) # length of sets

# add more items in sets
a.add(12258)
print("added", a)

# remove item from sets 
a.remove(12258)
print("removed", a)

# pop random item remove from sets 
a.pop()
print("random item removed", a)

# clear all item are clear from sets
a.clear()
print( "clear",a)  #output:set()



# union of sets all item from both sets
a1={1,3,5,6,8}
a2={2,4,6,8,10}
print("union " , a1.union(a2))

# intersection of sets common item from both sets
print("intersection", a1.intersection(a2))                                 




