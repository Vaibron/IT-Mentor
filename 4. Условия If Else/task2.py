'''Даны два числа. Вывести большее из них.'''

a, b = map(int, input().split())

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('Числа равны')