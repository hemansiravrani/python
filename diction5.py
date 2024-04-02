thisdict = {
    "name" : "a",
    "course" : "2",
        
}
mykeys =list(thisdict.keys())
mykeys.sort()
sortedDict = {i : thisdict[i] for i in mykeys}
print (sortedDict)