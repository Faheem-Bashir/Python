num1=float(input("Enter num 1: "))
operator=input("Enter an operator: ")
num2=float(input("Enter num 2: "))
if operator =="+":
    result=num1+num2
elif operator=="-":
    result=num1-num2
elif operator=="/":
    if num2==0:
       result="Cannot divide by zero"
    else:
        result=num1/num2
elif operator =="%":
    result=num1%num2
elif operator =="*":
    result=num1*num2
else: 
    result="Invalid Operator"
print(result)

######### even odd ########

n=int(input("Enter a number"))
if n%2==0:
    print("Even no.")
else:
    print("Odd")

########## Login ###########
username=input("Enter your username: ")
passw=input("Enter your password:")
if username == "faheem135":
    if passw == "123456":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")






        
