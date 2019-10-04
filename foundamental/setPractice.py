# add remove pop clear copy update
# issubset issuperset
# union intersection difference
# difference_update intersection_update update
# len()


set1 = set(range(10))

print(type(set1))

set2 = set('hello')
print(set2)

set3 = set(list([1,2,4,2]))
set4 = set([1,23,5,6,1])
set5 = set((1,2,3,'sjdfl',4,4))
print(set3)
print(set4)
print(set5)

set1.add('dd')
print(set1)

a = set1.pop()
print(set1)

set1.remove(3)
set1.clear()

b = set3.union(set4)
c = set3.difference(set4)
d = set3.intersection(set4)
frozenset(set([1,2,3]))
