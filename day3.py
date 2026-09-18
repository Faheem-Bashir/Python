###############  Lists  ################
lt=["faheem",20,63,88]
##############Accessing elements###############
print(lt[2])
################ Add elements in list  #########################
lt[3]=15 ## changes element at given index
print(lt)
lt.append(True) ## adds element at last
print(lt)
lt.insert(1,"wasiq") ## Adds element at specific location
print(lt)
##################### End ###################

################# Removing elements in list ##################
lst=[23,"Faheem", "wasiq", 99]
lst.remove(99) ## here we remove directly element
print(lst)
lst.pop(1)  ### here we remove by element
print(lst)
####################### End #################

######################### Slicing ########################
lte=[5,8,9,"faheem", False]
print(lte[1:4]) #### prints from index 1 to 4 (excluding 4)
print(lte[0:]) #### prints from index 0 to end 
print(lte[-2])  ### prints second last element
print(lte[:4]) ### prints from start to 4 element (excluding 4)
print(lte[::-1]) ## prints from last index to start (reverse order)
print(lte[0:5:2]) ## prints from 0 index but skips one element at each step
print(lte[::])  ## prints from start to end

tp=(10,5,8,0,8)
# print(type(tp))
print(tp[0])
print(tp)

ltt=[10,3,5,8]
ltt.insert(1,99)
print(ltt)

ltp=[20,32,'faheem',False, 78.3]
ltp[2]="wasiq"
print(ltp)








print(lte[::-2])
print(tp)
print(tp[0])
tp[1]="Faheem"