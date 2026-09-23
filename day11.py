# while True:
#     x=int(input("Enter a number: "))
#     for i in range(2,x):
#         if x%i==0:
#             print("Number is prime")
#             break
#     else:
#         print("Number is not prime")
#     choice=input("Do you want to continue: ")
#     if choice != 'yes':
#         break

# while True:
#     st=input("Enter a string: ")
#     word=st[::-1]
#     if st==word:
#         print("String is palindrome")
#     else:
#         print("string is not palindrome")
#     t=input("do you want to continue: ")
#     if t != 'yes':
        # break

while True:
    input1=float(input("Enter a number 1: "))
    op=input("Enter an operator: ")
    input2=float(input("Enter a number 2: "))
    if op=="+":
        print(input1+input2)
    elif op=="-":
        print(input1-input2)
    elif op=="*":
        print(input1*input2)
    elif op=="/":
        try:
            print(input1/input2)
        except ZeroDivisionError:
            print("Can't divide by zero")
    elif op=="%":
          try:
            print(input1%input2)
          except ZeroDivisionError:
                print("Can't divide by zero")    
    else:
        print("Invalid operator")
    c=input("Do you want to continue(Yes/No)").lower()
    if c!="yes":
        print("You quit")
        break
        
        

        