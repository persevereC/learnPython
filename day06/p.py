# 函数和模块

# c(m, n)
'''
def fac(num):
  result = 1
  for i in range(1, num+1):
    result *= i
  return result
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m-n))
'''


# 掷骰子
'''
from random import randint
def roll_dice(n=2):
  total = 0
  for _ in range(n):
    total += randint(1, 6)
  return total
def add(a=0, b=0, c=0):
  return a + b + c
def add(*args):
  total = 0
  for val in args:
    total += val
  return total
print(roll_dice(3))
print(add(1, 3, 5, 7, 9))
print(add)
'''


# 模块
'''
from module1 import foo
foo()
import module1 as m1
m1.foo()
'''


# __name__(__name__是Python中一个隐含的变量它代表了模块的名字，导入以下模块不会执行)
'''
def foo():
  pass
def bar():
  pass
if __name__ == '__main__':
  print('foo called')
  foo()
  print('bar called')
  bar()
'''










