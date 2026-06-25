mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)

print(mySet)

myFrozenSet = frozenset(mySet)

print(myFrozenSet)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

diffSet = set1 - set2
print(diffSet)
diffSet = set2.difference(set1)
print(diffSet)