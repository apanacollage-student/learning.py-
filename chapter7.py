#while loop=jab tak condition false na ho jab tak chale ga 
#ex
i=1
while(i<10): #ye 9 tak jaaye ga each sab ake ake baar check ho ga kon kon 10
    #se chhota hai or 10se jitna chhota ho ga sab print ho jaaye ga 
    print(i)
    i+=1

    
# display in .py 1to50 number using while loop
i=1
while(i<51):
    print(i)
    i+=1

# specific number print karwa shakte hai
for i in range(0,51,5):
    print(i)

#list in for loop
list=[1,2,4,7,4,7,4,7,4]
for i in list:
    print(i)

# use for loop with else condition
a=["ayush","yadav"]
for i in a:
    print(i)

else:
    print("done")



#brake in loop
for i in range(0,101):
    if(i==40):
        break
    print(i)


# -----------PRACTICE SET IN PYTHON------------#
#write a program to print multification tabel of a given number using for loop
number=int(input("enter your table:"))
for i in range(1,11):
    print(f"{number}={i} = {number*i}")

# -----------PRACTICE SET IN PYTHON------------#

#conver into while loop
n=int(input("enter table:"))
i=1
while(i<11):
    print(f"{n}*{i} = {n*i}")
    i+=1

# write a program to greet all the person names stored in a list "i"
# and which start with s 

list=["ayush","kumar","sahin","nikhil"]
for i in list:
    print(i.startswith("s"))
    print(f"hello{i}")

# write a program to find whether a given number or not
n=int(input("enter your number:"))
for i in range(2,n):
    if(n%i)==0:
        print("this is not prime number:")
        break

else:
    print("this is prime number")


#5 write a program to fimd the sum of first n natural number using while loop

n=int(input("enter number"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)


#6 write a program to calcculate the factorial of a given using loop
n=int(input("enter number"))
product=1
for i in range(1,n+1):
    product = product*i
print(f"the factriol of {n} is {product}")

#odd or even
n=int(input("enter your number:"))
if(n%2==0):
    print(n,"is even number")

else:
    print("is odd number")





# important A:write a program to print the following star
"""for m=3
..*
.***
*****
"""
n=int(input("enter a get star number:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")


#8 write a program flowing star print
"""
for n=3
*
**
***
****
"""
n=int(input("enter get star"))
for i in range(1,n+1):
    print(" "*(n-1),end="")
    print("*"* n,end="")
    print("")



#9 write a flowing star print
"""
***
*  * for n=3
***
"""
n=int(input("enter get star"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
     print("*",end="")
     print(" "*(n-2),end="")
     print("*",end="")
     print("")
    

    
# write a  table
n=int(input("enter table:" ))
for i in range(1,11):
    print(f"{n}*{i}= {n*i}")


#write a reversed table user give 
n=int(input("enter a table:"))
for i in range(1,11):
    print(f"{n}*{11-i}= {n*(11-i)}")