
#file banane or write karne ke lea
f=open("onefile.txt","w")
f.write("ayush you are expert in python")
f.close

#file ke content ko read karne ke lea
f=open("onefile.txt","r")
print(f.read())
f.close

# file me comment karne ke lea
f=open("onefile.txt","a")
f.write("\nthis is append ")
f.close()




#sab content ko indusial print kar shakte hain
f=open("onefile.txt","r")
lines=f.readline()
print(lines)
lines=f.readline()
print(lines)
f.close()

#sab content ko ake list me de ga
f=open("onefile.txt","r")
lines=f.readlines()
print(lines)

f.close()

#use with =with use karne pe close nahi karna parta hain
with open("onefile.txt","r") as f:
    data=f.read()
    print(data)

#agar ye content present hain to de ga nahi to nahi
with open("onefile.txt", "r") as f:
    content=f.read()
    if "yadav" in content:
        print("yes yadav is present in file!")
    else:
        print("yadav is not present ")


#################practice set##############################################################
#the game()function in a game lets a user play a game and ewturn a score as an intiger.you need a read a file'highscore.txt'which is either blank or contans the program to update the hi-score whenever the game function()brake the hi-score

import random
def game():
    print("you are playing...")
    score=random.randint(1,100)
    with open("highscore.txt") as f:
        hiscore=f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score is:{score}")
    if score>hiscore:
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score
game()


##the game()function in a game lets a user play a game and ewturn a score as an intiger.you need a read a file'highscore.txt'which is either blank or contans the program to update the hi-score whenever the game function()brake the hi-score
#but es me user se number lea hain

def game():
    print("you are playing!")
    score = int(input("enter your number: "))

   
  
    with open("score.txt", "r") as f:
            hiscore = f.read()
            if hiscore != "":
                hiscore = int(hiscore)
            else:
                hiscore = 0

    print(f"your score is: {score}")
   

    
    if score > hiscore:
        with open("score.txt", "w") as f:
            f.write(str(score))
        
    else:
        print("Try again!")

game()
print("successful!")


#3 write a program to genrate multiplecation table from 2to 20 and write it to the diffrent  file place these file in folder

def gentable(n):
    table=""
    for i  in range(1,11):
        table+= f"{n}*{i}={n*i}\n"

    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    gentable()




#4=a file contains a word "monkey" multiple times. you
#need to write a program which replace this word with
#=### by updating the some file
word="monkey"
with open("onefile.txt","r") as f:
    content=f.read()

newcontent=content.replace("monkey","###")
with open("onefile.txt","w") as f:
    f.write(newcontent)


#6=ake file me bahut sara content hain or us me python ko dhuna hain
#mila to yes nahi to no
with open("log.txt","r") as f:
    content=f.read()
    if "python" in content:
        print("yes python in logtxt file")
    else:
        print("no file is not found")


# 7=write a program to find out the line number where pthon is present from question no=6
with open("log.txt","r") as f:
    content=f.readlines()
    lineno=1
    for line in content:
        if "python" in line:
            print(f"yes python is present line no is:{lineno}")
            break
        lineno +=1
    else:
        print("python is not present")


#8=write a program to make a copy of a text file 
with open("log.txt","r")as f:
    copy=f.read()

with open("newlog.txt","w")as f:
    f.write(copy)


#9= wap to find a file is identical match the content of another file
with open("log.txt","r")as f:
    content1=f.read()
with open("newlog.txt","r") as f:
    content2=f.read()
    if content1==content2:
        print("yes these file is match")
    else:
        print("no these file is not match")



##########wap to wipe(khali) out the content of a file python
with open("newlog.txt","w")as f:
    content=f.write("")