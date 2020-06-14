"""
判断输入的正整数是不是回文数
"""

num = 0
num2 = 0
while num <= 0:
    num = int(input('请输入正整数：'))
temp = num
while temp > 0:
    num2 = num2 * 10 + temp % 10
    temp //= 10
if num == num2:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
input()