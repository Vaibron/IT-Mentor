"""Написать программу для нахождения среднего арифметического списка чисел. 
Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка), 
программа должна корректно обработать эту ошибку и выдать соответствующее сообщение. 
Информация об ошибках должна быть записана в лог."""

import logging

logging.basicConfig(filename="py_log3.log")

err = 'При вводе списка чисел была допущена ошибка'


def average(lst):
    num = sum(lst) / len(lst)
    return int(num)


try:
    lst = list(map(float, input('Введите числа через пробел: ').split()))
    print(average(lst))
except ValueError:
    logging.error("Ошибка: в списке имеются строки")
    print(err)
except ZeroDivisionError:
    logging.error("Ошибка: список чисел пуст")
    print(err)
except Exception as e:
    logging.error(f"Ошибка: {e}")
    print(err)
