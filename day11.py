while True:
    x=int(input("Enter a number: "))
    for i in range(2,x):
        if x%i==0:
            print("Number is prime")
            break
    else:
        print("Number is not prime")
    choice=input("Do you want to continue: ")
    if choice != 'yes':
        break

while True:
    st=input("Enter a string: ")
    word=st[::-1]
    if st==word:
        print("String is palindrome")
    else:
        print("string is not palindrome")
    t=input("do you want to continue: ")
    if t != 'yes':
        break

