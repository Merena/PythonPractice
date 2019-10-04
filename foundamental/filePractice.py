'''
    open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text)
    rt wt at xt
    rb wb ab xb
    r+ w+ a+

    ======================
    _io.py
'''

import io
import fileinput

print('io:', dir(io), '\n')

io.open    # in _io.py
io.BytesIO

f = open('randomPractice.py', 'rt')
print(dir(f))
print(type(f))

b = f.readlines()
print(b)

f.seek(0)

# Read from underlying buffer until we have n characters or we hit EOF.
# If n is negative or omitted, read until EOF.
c = f.read()

f.seek(0)
d = f.read(10)


a = 1