'''Даны три числа. Найти наименьшее из них.'''

a, b, c = map(int, input().split())

min = a
if b < min:
    min = b
elif c < min:
    min = c

print(min)