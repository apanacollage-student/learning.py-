# start with chapter 3
# slicing
name="ayush"
nameshort=name[0:1]
print(nameshort)

# kisi eke character ko print karna hai to
name="ayush"
character=name[0]
print(character)

# negative slicing can also used
name="aniket"
print(name[-4:-1])

# lenth function
name="indian institute of business management"
print(len(name)) 
print(name.endswith("ment"))
print(name.capitalize())
print(name.replace("indian","INDIAN"))
print(name.find("business"))

a='ayush yadav' # replace function
a=a.replace("ayush yadav","aniket yadav")
print(a)

# find function
a="ayush yadav"
a=a.find("h")
print(a)
# next line \n , \t , \\
a="dear ayush,\n this is your first letter"
print(a)

#chapter 3 practice
