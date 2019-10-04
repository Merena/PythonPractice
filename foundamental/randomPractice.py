import random

print('random:', dir(random), '\n')

print(random.randint(1,8))
print(random.randrange(4,10,2))
print(random.sample(range(1,70), 10))
print(random.uniform(4,20.5))
print(random.choice(list(range(4,60))))
print(random.random())
