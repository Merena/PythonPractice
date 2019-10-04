### 1、 __init__.py
__init__.py 文件的作用是将文件夹变为一个Python模块,Python 中的每个模块的包中，都有__init__.py 文件。
我们在导入一个包时，实际上是导入了它的__init__.py文件。这样我们可以在__init__.py文件中批量导入我们所需要的模块，而不再需要一个一个的导入。

### 2、__all__
在模块的一开始定义 __all__ 变量，import该模块后，只能找到 __all__中存在的变量或者函数，其他的不能调用

### 3、as
如果import的语句比较长，导致后续引用不方便，可以使用as语法，
import modulename as name  # 只能通过name来引用
from modulename import attrname as name  # 只能通过name来引用

### 4、with语句
使用with语句的目的就是把代码块放入with中执行，with结束后，自动完成清理工作，无须手动干预

### 5、Iterable and Iterator
判断是不是可以迭代，用Iterable

from collections import Iterable  

isinstance({}, Iterable) --> True  
isinstance((), Iterable) --> True  
isinstance(100, Iterable) --> False  
 
判断是不是迭代器，用Iterator

from collections import Iterator  
isinstance({}, Iterator)  --> False  
isinstance((), Iterator) --> False  
isinstance( (x for x in range(10)), Iterator)  --> True  

所以，
凡是可以for循环的，都是Iterable
凡是可以next()的，都是Iterator
集合数据类型如list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象

python学习之Iterable和Iterator的区别
https://blog.csdn.net/zoulonglong/article/details/80887244

Iterable：由英文的命名规则知道，后缀是able的意思就是可怎么样的，因此iterable就是可迭代的意思。

Iterator：由英文的命名规则知道，后缀是or或者er的都是指代名词，所以iterator的意思是迭代器。

isinstance('abc', Iterable)

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
>>> isinstance([], Iterator)
False

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：

>>> isinstance(iter([]), Iterator)
True

总结：
凡是可作用于for循环的对象都是Iterable类型；
凡是可用作next()函数的对象都是Iterator类型，它表示一个惰性计算的序列。
集合数据类型如list，dict，str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

### 6、lambda
lambda [arg1[, arg2, ... argN]]: expression
lambda是一个表达式，而不是一个语句（lambda is an expression, not a statement.）。
lambda的主体是一个单个的表达式，而不是一个代码块

lambda x:True if x % 3 == 0 else False

### 7、函数式编程
Python提供了很多函数式编程的特性，如：map、reduce、filter、sorted等这些函数都支持函数作为参数，lambda函数就可以应用在函数式编程中。

### 8、Python中的各种推导式
https://www.cnblogs.com/tkqasn/p/5977653.html

https://www.cnblogs.com/loved/p/8671149.html


