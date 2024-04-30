'''Найти факториалы чисел от 1 до 5 (включительно).'''

for n in range(1, 6):
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)