import os

# all functions from posix or nt
# 包含 posix.py ntpath.py os.py genericpath.py
# posix.py中的方法用os.调用，ntpath.py和genericpath.py中的方法用os.path调用

# os.getenvb('PATH')
# os.putenv('PATH', os.getcwd())
# os.path.split()
# os.path.samestat()
# os.path.sameopenfile()
# os.path.basename()
# os.path.exists()

print('os:', dir(os), '\n')
print('os.path', dir(os.path))

print(os.getcwd())

print(os.listdir(os.getcwd()))
os.chdir('../')
print(os.getcwd())
print(os.listdir(os.getcwd()))

if not os.path.exists('newPath1'):
    os.mkdir('newPath1')

if not os.path.exists('newPath1'):
    os.mkdir('newPath1', 0o377)

try:
    os.makedirs('x/y/z')
    os.removedirs('x/y/z')
except BaseException as e:
    print(e)

try:
    os.rmdir('newPath1')
except BaseException as e:
    print(e)

if not os.path.exists('mydir'):
    os.mkdir('mydir')
    os.rename('mydir', 'yourdir')

if not os.path.exists('bill/mike/zolin'):
    os.makedirs('bill/mike/zolin')
    os.renames('bill/mike/zolin', 'a/b/c')

if os.path.exists('a/aa.txt'):
    os.remove('a/aa.txt')

