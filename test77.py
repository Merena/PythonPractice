from fractions import Fraction
import fractions

'''
编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''


def calc(end):
    start = 2 if end%2 == 0 else 1
    sum = Fraction()

    for i in range(start, end+1, 2):
        sum = sum + Fraction(1, i)
        print(sum)

    return sum

a = calc(100)
