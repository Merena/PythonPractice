'''
there are four enumeration classes that can be used to define unique sets of names and values:
Enum, IntEnum, Flag, and IntFlag.
It also defines one decorator, unique(), and one helper, auto
'''

from enum import *

# print('enum:', dir(enum), '\n')

# print(help(enum))

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3


for a in Shake:
    print(a)


apples = {}
apples[Color.RED] = 'red delicious'


class Color2(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()

print(list(Color))

for name, member in Shake.__members__.items():
    print(name, member)