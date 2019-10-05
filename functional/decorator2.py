#
# https://blog.csdn.net/adsadadaddadasda/article/details/80769294
#

import functools

def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        a = fn()
        print("goodby, %s" % fn.__name__)

        return a
    return wrapper


@hello
def foo():
    return 555

print(foo())


def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"


print(hello())


def salesgirl(discount):
    def expense(method):
        def serve(*args):
            print("Salesgirl:Hello, what do you want?", method.__name__)
            result = method(*args)
            if result:
                print("Salesgirl: This shirt is 50$.As an old user, we promised to discount at %d%%" % (discount))
            else:
                print("Salesgirl: Well, how about trying another style?")
            return result

        return serve

    return expense


@salesgirl(50)
def try_this_shirt(size):
    if size < 35:
        print("I: %d inches is to small to me" % (size))
        return False
    else:
        print("I:%d inches is just enough" % (size))
        return True


result = try_this_shirt(38)
print("Mum:do you want to buy this?", result)