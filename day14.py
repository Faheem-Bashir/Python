########### filtering out the fruits having length more than 3 ##################
fruits=['mango',"apple","kiwi","custardapple"]
f=list(filter(lambda x:len(x)>3,fruits))
print(f)

######################### finding maximum in array #######################
lt=[12,100,17,29,200,588,28,300]
lt.sort()
print(lt[-1])

#################### finding minimum in array using min function #####################
print(min(lt))

####################### filtering out numbers divisible by 3 ####################
ltt=[12,89,27,20,21,30]
new=list(filter(lambda x:x%3==0,ltt))
print(new)

##################### Remove duplicates from the element #######################

let=[12,5,12,2,2,5,6,9,10,9,6]
newLt=list(set(lt))
print(newLt)

####################### Swaping ################
a=10
b=30
a,b=b,a
print("a=", a)
print("b=", b)
