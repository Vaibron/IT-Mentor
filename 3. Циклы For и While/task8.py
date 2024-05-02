'''Найти все простые числа от 2 до 50.'''

lst = []
for i in range(2, 51):
    flag = True
    for j in range(2, i):
        if i%j == 0:
            flag = False
            break
    if flag:
        lst.append(i)

print(*lst)