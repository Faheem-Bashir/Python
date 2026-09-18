########### Nested dictionary #######

students={
    "1":{"name":"faheem","roll-no":21,"address":"pulwama"},
    "2":{"name":"wasiq","roll-no":24,"address":"srg"}
}

students["3"]={"name":"towheed","address":"pul","roll-no":"25"} ## adds a key value pair in dictionary
del students["1"] ### deletes the key
students["2"]["name"]="zahid" #### updates the value
print(students)

print(students.keys())


######## Nested List#######
lt=[["faheem",12,"sahil"],["zahid",44,True],["asif",88,0]] 
print(lt[0][1]) ### prints the value 1 in index 0
lt[0].append("shahid") ### adds the value in index 0
lt[0].insert(1,45) ### adds the value at index 1 in index 0
print(lt)




# studens={
#    "studen1": {"name":"faheem",
#       "roll-no":10,""
#       "address":"Pulwama",
#       "subjects":{"subject1":{"name":"engliah","name2":"grammar"},
#                   "subject2":"Computer"}},
#      "studen2": {"name":"zahid", 
#        "roll-no":33,
#        "address":"kakapora"}
# }
