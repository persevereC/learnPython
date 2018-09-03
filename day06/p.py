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


# 最大公约数 最小公倍数
'''
def gcd(x, y):
  if x > y:
    (x, y) = (y, x)
  for factor in range(x, 1, -1):
    if x % factor == 0 and y % factor == 0:
      return factor
    return 1
def lcm(x, y):
  return x * y // gcd(x, y)
print(gcd(2, 5))
print(lcm(2, 5))
'''


# Python的内置函数
# 	- 数学相关: abs / divmod / pow / round / min / max / sum
# 	- 序列相关: len / range / next / filter / map / sorted / slice / reversed
# 	- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
# 	- 数据结构: dict / list / set / tuple
# 	- 其他函数: all / any / id / input / open / print / type


# Python常用模块
# 	- 运行时服务相关模块: copy / pickle / sys / ...
# 	- 数学相关模块: decimal / math / random / ...
# 	- 字符串处理模块: codecs / re / ...
# 	- 文件处理相关模块: shutil / gzip / ...
# 	- 操作系统服务相关模块: datetime / os / time / logging / io / ...
# 	- 进程和线程相关模块: multiprocessing / threading / queue
# 	- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
# 	- Web编程相关模块: cgi / webbrowser
# 	- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...



