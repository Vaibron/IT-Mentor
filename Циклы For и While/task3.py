'''Напишите программу для вывода таблицы умножения от 0 до 9.
Используйте вложенный цикл for, print и range'''


for i in range(1, 11):
    for j in range(1, 10):
        print(j, '*', i, '=', j*i, end='\t')
    print()