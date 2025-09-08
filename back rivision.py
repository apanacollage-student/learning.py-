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