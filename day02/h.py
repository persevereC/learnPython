# a = int(input('a = '))
# b = int(input('b = '))

# print('%d + %d = %d' % (a, b, a+b))
# print('%d - %d = %d' % (a, b, a-b))
# print('%d * %d = %d' % (a, b, a*b))
# print('%d / %d = %f' % (a, b, a/b))
# print('%d // %d = %d' % (a, b, a//b))
# print('%d %% %d = %d' % (a, b, a%b))
# print('%d ** %d = %d' % (a, b, a**b))

# 华氏转摄氏（F = 1.8C + 32）
f = float(input('华氏温度 = '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 计算圆的周长面积
import math
radius = float(input('半径 = '))
perimeter = 2 * math.pi * radius
area = math.pi * radius *radius
print('圆的周长为%.2f，面积为%.2f' % (perimeter, area))

# 判断闰年
year = int(input('年份 = '))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)
