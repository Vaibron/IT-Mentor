'''Даны три целых числа. Найти количество положительных чисел в исходном наборе.'''

a, b, c = map(int, input().split())

count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1

print(count)