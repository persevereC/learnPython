# 字符串

# 列表list ['a', 'b', 'c']

# 元组 ('a', 'b', 'c') 无法修改

# 字典 {name: 'll', age: 20}


# 跑马灯
'''
import os
import time
def main():
  content = 'happy day to cl '
  while True:
    os.system('clear')
    print(content)
    time.sleep(0.5)
    content = content[1:] + content[0]
if __name__ == '__main__':
  main()
'''


# 验证码
import random
def generate_code(code_len=4):
  all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  last_pos = len(all_chars) - 1
  code = ''
  for _ in range(code_len):
    index = random.randint(0, last_pos)
    code += all_chars[index]
  print(code)
generate_code()


