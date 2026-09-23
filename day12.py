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


def palindrome(st):
    reverse=st[::-1]
    if reverse==st:
        print("string is palindrome")
    else:
        print("strng is not palindrome")


st=input("Enter a string")
palindrome(st)

def sq(x):
    print(x*x)
sq(10)