'''Даны два числа. Вывести вначале большее, а затем меньшее из них.'''

a, b = map(int, input().split())

if a > b:
    print(f"Большее число: {a}, Меньшее число: {b}")
elif b > a:
    print(f"Большее число: {b}, Меньшее число: {a}")
else:
    print("Числа равны")