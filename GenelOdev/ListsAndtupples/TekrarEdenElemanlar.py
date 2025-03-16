myList=["Ali","Kemal","Yavuz","Mehmet","Mustafa","Yavuz","Mehmet","Mustafa"]

newList=[]

for item in myList:
    if item not in newList:
        newList.append(item)
print(newList)