"""Написать программу для генерации случайных чисел в заданном диапазоне. 
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), 
программа должна вывести ошибку и попросить ввести диапазон заново. 
Информация об ошибках должна быть записана в лог."""

import random
import logging

logging.basicConfig(filename="py_log1.log")


def random_numbers(a, b):
    num = random.randint(a, b)
    return num


try:
    a, b = map(int, input(f'ВCведите диспазон чисел от 0 до ꝏ : ').split())
    if a > 0 and b > 0:
        print(random_numbers(a, b))
    else:
        raise Exception('Границы диапазона меньше нуля')

except Exception as e:
    logging.error(e)
    print(f'Ошибка: {e}. Введите диапазон значений заново')
