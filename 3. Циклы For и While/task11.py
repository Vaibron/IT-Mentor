'''Найти факториалы чисел от 1 до 5 (включительно).'''

# for n in range(1, 6):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     print(f)

n = 5
for i in range(n):
    for j in range(n):
        if n//2 == j or n//2 == i:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()