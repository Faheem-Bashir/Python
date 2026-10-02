########## HANDLING KEY ERROR ############

dt={
    "name":"faheem",
    "address":"Pulwama"
}

try:
    print(dt["class"])
except KeyError:
    print("Key not found")
 #################### END ##########################

try:
    print(a)
except NameError:
    print("variable not defined")