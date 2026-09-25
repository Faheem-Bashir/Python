 ############################ Lambda function ######################
add= lambda x,y: x+y
print(add(12,3))

################## Positive Negative using lambda ##############
posNeg= lambda x: "negative" if x<0 else "postive"
print(posNeg(12))

######################### Convert string to int using MAP ######################
lt=["12","23","0","55"]
new=list(map(int,lt))
print(new)

######################### Convert lower to upper case using MAP ######################
names=["faheem","wasiq","towheed"]
new2=list(map(str.upper,names))
print(new2)

###################################### Filter ##############################
data=[2,3,4,5,6,7,8,10,11,17,20]
new3=list(filter(lambda x: x%2==0,data))
print(new3)




