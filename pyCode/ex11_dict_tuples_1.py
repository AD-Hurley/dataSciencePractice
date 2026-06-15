popDict={"China":143,"India":136,"USA":32,"Pakistan":21}


usrInput=input("Either Enter <print> to print population data, <add> to add an entry to the dictionary, or <remove> to remove and entry: ")

if usrInput == "print":
    for key,value in popDict.items():
        print(key,"==>",value)
elif usrInput == "add":
    newCountry=input("Enter new country: ")
    newPop=input("Enter new population: ")
    popDict[newCountry]=newPop
    for key,value in popDict:
        print(key,"==>",value)
elif usrInput == "remove":
    delCountry=input("Enter country to remove: ")
    del popDict[delCountry]
    for key,value in popDict.items():
        print(key,"==>",value)
else:
    print("Invalid input")

print(popDict)
usrInput=input("Enter a country from the table:")
if usrInput in popDict:
    print(popDict[usrInput])
else:
    print("Invalid input")
