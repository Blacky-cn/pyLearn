"""
输出100以内所有的素数

素数指的是只能被1和自身整除的正整数（不包括1）
"""

for n in range(2, 100):
    prime = 1
    for a in range(1, n // 2 + 1):
        if (n % a == 0) and (a != 1) and (a != n):
            prime = 0
            break
    if prime == 1:
        print(n, end = ' ')
input()