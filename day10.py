# ###### Check if a string is palindrome or not ################
# st=input("Enter a string: ")
# reverse=""
# for char in st:
#     reverse=char+reverse
# if reverse==st:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")

# ######################## END #########################

 ############################### Star Traingle #######################

# n=5
# for i in range(0,5):
#     print("*"*i)
# # ######################## END #########################

#  ############################### Reverse Star Traingle #######################
# x=5
# for i in range(5,0,-1):
#     print("*"*i)
# ######################## END #########################

######################### Error handling ###################
########################### zero division error #####################
try:
    print(10/0)
except ZeroDivisionError:
    print("Can't divide by zero")
########################### Attribute error #####################
try:
    st="wasiq"
    st.append("a")
    print(st)
except AttributeError:
    print("No such feature exists")
# try:
#     age=13
#     if age>18:
#     print("adult")
# except IndentationError:
#     print("indentation wrong")
try:
    lt=["hello",20,30]
    print(lt[5])
except IndexError:
    print("index does not exist")

try:
    print(10+"hello")
except TypeError:
    print("cant add string to integer")

try:
    a=int(input("Enter a number: "))
    print(a)
except ValueError:
    print("cant convert string to int")
# try:
#     n=5'
#     print(n)
# except SyntaxError:
#     print("hi")
try:
    print(n)
except NameError:
    print("varible not defined")