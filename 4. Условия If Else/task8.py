'''Даны два целых числа: D (день) и M (месяц),
определяющие правильную дату невисокосного года.
Вывести значения D и M для даты, следующей за указанной.'''

D, M = map(int, input().split())

match M:
    case 1, 3, 5, 7, 8, 10:
        match D:
            case 31:
                M += 1
                D = 1
            case _:
                D += 1
    case 4, 6, 9, 11:
        match D:
            case 30:
                M += 1
                D = 1
            case _:
                D += 1
    case 2:
        match D:
            case 28:
                M += 1
                D = 1
            case _:
                D += 1
    case 12:
        match D:
            case 31:
                M, D = 1, 1
            case _:
                D += 1

print(D, M)
