###################### Check prime using function ############
def prime(x):
    if x<=1:
        print("not prime")
    else:
        for i in range(2,x):
            if x % i==0:
                print("Not prime")
                break
        else:
            print("number is prime")

num=int(input("Enter a number: "))
prime(num)


###################### Check Palindrome using function ############

def palindrome(st):
    reverse=st[::-1]
    if reverse==st:
        print("string is palindrome")
    else:
        print("string is not palindrome")

st=input("Enter a string")
palindrome(st)


###################### Square of a number using function ############
value=int(input("Enter a number: "))
def sq(x):
    print(x*x)
sq(value)



###################### Calculator using function ############

def cal(num1,operator,num2):

    if operator =="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="/":
        try:
            result=num1/num2     
        except ZeroDivisionError:
            result="Can't divide by zero"
    elif operator =="%":
        result=num1%num2
    elif operator =="*":
        result=num1*num2
    else: 
        result="Invalid Operator"
    print(result)

num1=float(input("Enter num 1: "))
operator=input("Enter an operator: ")
num2=float(input("Enter num 2: "))
  
cal(num1,operator,num2)