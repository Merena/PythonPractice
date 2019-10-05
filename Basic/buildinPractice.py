print(dir(), '\n\n')

print(dir(__builtins__), '\n\n')

print(__file__, '\n\n')

print(__name__, '\n\n')

print('str:', dir(str(333)), '\n\n')
print('bool:', dir(bool(True)), '\n\n')
print('int:', dir(int(333)), '\n\n')
print('float:', dir(float(333)), '\n\n')
print('list:', dir(list((333,99))), '\n\n')
print('tuple:', dir(tuple([333,99])), '\n\n')
print('set:', dir(set([333,99])), '\n\n')
print('dict:', dir(dict({'4':2})), '\n\n')
print('bytes:', dir(bytes), '\n')
print('bytearray:', dir(bytearray), '\n')

# a = True.to_bytes()
b = 4
c = b.bit_length()
# d = b.to_bytes()
# e = int.from_bytes(d)

f = [8,1,3,4,5]
f.sort()
f.append(6)
f.append([7,8])
g = f.count(4)
h = f.index(5)
f.insert(0,9)
f.remove(9)
f.clear()

'''
tuple
'''

a1 = (8,1,3,4,5,1)
b1 = a1.count(1)
c1 = a1.index(1)

print('')
