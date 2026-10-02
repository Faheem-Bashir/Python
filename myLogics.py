# ######  sum of a digits of a number ##############
# num=input("Enter a number")
# sum=0
# for i in num:
#     cv=int(i)
#     sum=sum+cv
# print(sum)
# ################## END #######################


# ###### Reversing a number ######
# number=input("enter a number: ")
# Tc=int(number[::-1])
# print(Tc)
# ######################## END ####################


# ##### checking number is palindrome or not #######
# number2=input("Enter a number")
# store=int(number2)
# cast=int(number2[::-1])
# if store == cast:
#     print("palindrom")
# else:
#     print("Not palindrome")
# # ######################### END #######################


# ####### reversing a string ###########################
# st=input("Enter a string")
# print(st[::-1])
# # ######################### END #######################


# ################ String palindrome ######################
# stt=input("Enter a string")
# store=stt
# reverse=stt[::-1]
# if store == reverse:
#     print("String is palindrome")
# else:
#     print("Strintg is not palindrome")
# # ######################### END #######################


# range1=10
# range2=20
# while range1<range2:
#     # flag=0
#     for i in range(2,range1):
#         if range1%i==0:
#             # flag=1
#             break
#     # if flag==0:
#     else:
#         print(range1)
#     range1=range1+1


# fact=1
# num=5    
# for i in range(1,num+1):
#     fact=fact*i;
# print(fact)

# lt=["12","23","0","55"]

# new=[]
# for i in lt: 
#     new.append(int(i))
# print(new)

# names=["faheem","wasiq","towheed"]
# new2=[]
# for i in names:
#     new2.append(i.upper())
# print(new2)

# data=[2,3,4,5,6,7,8,10,11,17,20]
# new3=[]
# for i in data:
#     if i%2==0:
#         new3.append(i)
# print(new3)



# def primeRange(r1):
#         if r1<=1:
#             flag=0
#         else:
#             for i in range(2,r1):
#                 if r1%i==0:
#                      flag=0
#                      break
#             else:
#                 flag=1
#         return flag

# nt=[1,2,3,8,9,5,15,19,26,27,53,7]
# newnt=list(filter(primeRange,nt))
# print(newnt)
# inn=int(input("Enter a number: "))
# result=primeRange(inn)
# if primeRange(inn)==1:
#      print("Number is prime")
# else:
#      print("Number is not prime")

rev=""
st="hello"
for i in st:
     rev=i+rev
print(rev)


 