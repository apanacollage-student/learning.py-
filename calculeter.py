num1=float(input("enter your 1st number: "))
num2=float(input("enter your 2nd number: "))
print("salect your operaters:[+ - * /]")
op=input("enter your operaters:")
if op=="+":
    print("the result is:",num1+num2)
elif op=="-":
    print("the relult is:",num1-num2)
elif op=="*":
    print("the result is:",num1*num2)
elif op=="/":
    if num2 !=0:
        print("the result is:",num1/num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("error: wrong operater")
