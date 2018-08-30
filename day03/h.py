# 2018/08/30 分支结构


# 身份验证
'''
name = input('name: ')
password = input('password: ')
if name =='cl' and password == '66':
  print('all is well~')
else:
  print('change')
'''


# 分段函数求值
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)
'''
x = float(input('x = '))
if x > 1:
  y = 3 * x - 5
elif x >= -1:
  y = x + 2
else:
  y = 5 * x + 3
print('f(%.2f) = %.2f' % (x,y))
'''


# 分段函数求值
# 		3x - 5	(x > 1)
# f(x) =	x + 2	(-1 <= x <= 1)
# 		5x + 3	(x < -1)
'''
x = float(input('x= '))
if x > 1:
  y = 3 * x -5
else:
  if x >= -1:
    y = x + 2
  else:
    y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))
'''


salary = float(input('本月收入: '))
insurance = float(input('五险一金: '))
diff = salary - insurance - 3500
if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 1500:
	rate = 0.03
	deduction = 0
elif diff < 4500:
	rate = 0.1
	deduction = 105
elif diff < 9000:
	rate = 0.2
	deduction = 555
elif diff < 35000:
	rate = 0.25
	deduction = 1005
elif diff < 55000:
	rate = 0.3
	deduction = 2755
elif diff < 80000:
	rate = 0.35
	deduction = 5505
else:
	rate = 0.45
	deduction = 13505
tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))



