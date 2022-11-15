MyList =[5+5,"orange",45,4.3,True]
print(MyList)
print(type(MyList[2]))

for item in MyList:
    print("{} is of the data type {}".format(item,type(item)))