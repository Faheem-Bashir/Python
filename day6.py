### Nested lists######
lt=[[["faheem",True,10],["zahid",33,"wasiq"]],  [["shahid","ubaid",False],[10,19,88]],  [["owasi","taheed","khalid"],["arif",10,99]]]

print(lt[0][1][2])
###### update data in list #####
lt[0][1][2]="ubaid"
# print(lt)
##### Add data in list ####
lt[2][0].append("ariz") ## by value
lt[1][0].insert(2,"rayees") ## by index
print(lt)


### Nested dictionary #####

dt={
    1:{"name":{"fname":"zahid","lname":"bashir"},"address":{"pincode":192304,"district":"pulwama"}},
     2:{"name":{"fname":"shahid","lname":"Malid"},"address":{"pincode":192301,"district":"srg"}},
    3:{"name":{"fname":"owais","lname":"rahid"},"address":{"pincode":192001,"district":"islambad"}}
}
##### Access values ######
print(dt[1]["name"]["lname"])
####### add values #######
dt[4]={"name":{"fname":"owais","lname":"rahid"},"address":{"pincode":192001,"district":"Kulgam"}}


### delete values #####
print(dt[4]["address"])
del dt[4]["address"]     
print(dt)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       