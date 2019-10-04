x,y,z = 1,2,3                # 使用序列解包方式进行赋值
print(x,y,z)

x,y = y,x                    #  利用序列解包交换x和y的值
print(x,y)

# x,y,z = 1,2              # 抛出异常
# x,y = 1,2,3              # 抛出异常

x = y = 20                    #  使用链式赋值设置x和y
print(x,y)

x *= 2                    #  增量赋值
x %= 3                    #  增量赋值
print(x)