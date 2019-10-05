import itertools

# a = itertools.product('1234', repeat=3)
#
# for aa in a:
#     print(aa)
#
# Combinatoric iterators

print('itertools product\n')

b = itertools.product('1234', repeat=2)
c = itertools.product('1234', repeat=3)

d = itertools.product('1234','678', repeat=1)
a = itertools.product('1234','678', repeat=2)

for aa in b:
    print(aa)

for aa in c:
    print(aa)

for aa in d:
    print(aa)

for aa in a:
    print(aa)

print('itertools permutations\n')

"""
    permutations(iterable[, r]) --> permutations object

    Return successive r-length permutations of elements in the iterable.

    permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
    """
b = itertools.permutations('1234', 2)
c = itertools.permutations('1234', 3)

for aa in b:
    print(aa)

for aa in c:
    print(aa)

# 对于 ``combinations()`` 来讲，元素的顺序已经不重要了
print('itertools combinations\n')

b = itertools.combinations('1234', 2)
c = itertools.combinations('1234', 3)

for aa in b:
    print(aa)

for aa in c:
    print(aa)
# 允许同一个元素被选择多次
print('itertools combinations_with_replacement\n')

b = itertools.combinations_with_replacement('1234', 2)
c = itertools.combinations_with_replacement('1234', 3)

for aa in b:
    print(aa)

for aa in c:
    print(aa)

print('itertools Infinite iterators\n')

a2 = itertools.count(4,3)
for aa in a2:
    if aa > 50:
        break
    print(aa)


b2 = itertools.cycle('abcd')
i = 0
for aa in b2:
    i=i+1
    if i > 20:
        break
    print(aa)

c2 = itertools.repeat('a', 20)
for aa in c2:
    print(aa)


print('Iterators terminating on the shortest input sequence\n')

a1 = list(range(1,20))
b1 = itertools.accumulate(a1)
for aa in b1:
    print(aa)

c1 = itertools.chain(b,c)
for aa in c1:
    print(aa)

d1 = list(range(5,10))
f1 = [True if x % 2 == 0 else False for x in range(1,6)]
g1 = itertools.compress(d1,f1)
for aa in g1:
    print(aa)

print('\ndropwhile')
a3 = itertools.dropwhile(lambda x : x<5, range(0,10))
for aa in a3:
    print(aa)

print('\ntakewhile')
b3 = itertools.takewhile(lambda x : x<5, range(0,10))
for aa in b3:
    print(aa)

print('\nfilterfalse')
c3 = itertools.filterfalse(lambda x : x<5, [3,7,4,8,1,9])
for aa in c3:
    print(aa)

print('\ngroupby')

# a4 = itertools.groupby(list(range(1,100),))