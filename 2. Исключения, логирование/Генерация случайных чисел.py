"""Написать программу для генерации случайных чисел в заданном диапазоне. 
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), 
программа должна вывести ошибку и попросить ввести диапазон заново. 
Информация об ошибках должна быть записана в лог."""

import random
import logging

logging.basicConfig(filename="py_log.log", filemode="w" )


def random_numbers(a, b):
    num = random.randint(a, b)
    return num


a, b = map(float, input(f'Введите диспазон чисел от 0 до ꝏ').split())

try:
    if a > 0 and b > 0:
        print(random_numbers(a, b))
    else:
        logging.error('Ошибка: границы диапазона меньше нуля')
        raise Exception('Error: Введите диапазон значений заново') 
    
except Exception as e:
    print(e)



