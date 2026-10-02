######$###### Check if a number is in list or not #####################################

lt=[10,22,68,88,18]
n=int(input("Enter a number: "))
flag=0
for i in lt:
    if n==i:
     flag=1
    break
if flag==1:
    print(n,"is in the list")
else:
    print(n,"is not in the list")

################### Check if a number is prime or not #####################################

x=int(input("Enter a number: "))
if x<=1:
    print("Not prime")
else:
    for i in range(2,x):
        if x%i==0:
            print(x,"is not prime")
            break  ############# exist the loop #########
    else:
        print(x,"is prime")
###### Check if a key exists in dictionary or not #####################################

dt={
    "name":"faheem",
    "roll-no":135,
    "address":"Pulwama"
}
l=input("Enter a key: ")
for key,value in dt.items():
    if key==l:
        print(key,":",value)
        break
else:
        print("Key not found")



