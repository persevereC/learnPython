# 循环结构
# range(101)可以产生一个0到100的整数序列。
# range(1, 100)可以产生一个1到99的整数序列。
# range(1, 100, 2)可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量。

'''
sum = 0
for i in range(10):
  sum += i
print(sum)
'''


'''
import random
answer = random.randint(1, 10)
print(answer)
counter = 0
while True:
  counter += 1
  number = int(input('请输入：'))
  if number < answer:
    print('bigger')
  elif number > answer:
    print('smaller')
  else:
    print('bingo')
    break
print('你总共猜了%d次' % counter)
if counter > 6:
  print('智商不足。。。')
'''


# 九九乘法表
'''
for i in range(1, 10):
  for j in range(1, i+1):
    print('%d*%d=%d' % (i, j, i*j), end = '\t')
  print()
'''


# 判断素数
'''
from math import sqrt
num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for i in range(2, end + 1):
  if num % i == 0:
    is_prime = False
    break
if is_prime and num != 1:
  print('%d是素数' % num)
else:
  print('%d不是素数' % num)
'''


# 最大公约数 最小公倍数
'''
x = int(input('x = '))
y = int(input('y = '))
if x > y:
  (x, y) = (y, x)
for factor in range(x, 0, -1):
  if x % factor == 0 and y % factor == 0:
    print('%d和%d的最大公约数是%d' % (x, y, factor))
    print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
    break
'''


# 三角形
row = int(input('请输入行数'))
for i in range(row):
  for _ in range(i + 1):
    print('*', end='')
  print() 
for i in range(row):
  for j in range(row):
    if j < row - i - 1:
      print(' ', end='')
    else:
      print('*', end='')
  print()
for i in range(row):
  for _ in range(row - i - 1):
    print(' ', end='')
  for _ in range(2 * i + 1):
    print('*', end='')
  print()