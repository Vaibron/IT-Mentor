'''Вывести все числа от 1 до 100, которые делятся на 3 без остатка.'''

for i in range(1, 101):
    if i%3 == 0:
        print(i, end=' ')

print()

for j in range(3, 101, 3):
    print(j, end=' ')