# 百钱百鸡问题，1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡（穷举法）
'''
for x in range(20):
  for y in range(33):
    z = 100 - x - y
    if 5*x + 3*y + z/3 == 100:
      print('%d只公鸡，%d只母鸡，%d只小鸡' % (x, y, z))
'''

# 斐波那契数列
'''
a = 0
b = 1
for _ in range(10):
  (a, b) = (b, a+b)
  print(a, end=' ')
'''


# 找出100~999之间的所有水仙花数(各位立方和等于这个数本身的数)
'''
for i in range(100, 1000):
  low = i % 10
  mid = i // 10 % 10
  high = i // 100
  if i == low ** 3 + mid ** 3 + high ** 3:
    print(i)
'''


# 回文数
'''
num = int(input('请输入一个正整数：'))
temp = num
num2 = 0
while temp > 0:
  num2 *= 10
  num2 += temp %10
  temp //= 10
if num == num2:
  print('%d是回文数' % num)
else:
  print('%d不是回文数' % num)
'''


# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
import time
import math
start = time.clock()
for num in range(1, 10000):
	sum = 0
	for factor in range(1, int(math.sqrt(num)) + 1):
		if num % factor == 0:
			sum += factor
			if factor > 1 and num / factor != factor:
				sum += num / factor
	if sum == num:
		print(num)
end = time.clock()
print("执行时间:", (end - start), "秒")


