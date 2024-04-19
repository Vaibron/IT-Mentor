"""Написать программу для генерации случайных чисел в заданном диапазоне. 
Если пользователь ввел недопустимые границы диапазона (например, меньше нуля), 
программа должна вывести ошибку и попросить ввести диапазон заново. 
Информация об ошибках должна быть записана в лог."""

import random
import logging
logging.basicConfig(level=logging.DEBUG, filename="py_log.log", filemode="w" )

def random_numbers(a, b):
    num = random.randint(a, b)
    logging.info('Генерируем рандомное число')
    return num



a, b = map(float, input(f'Введите диспазон чисел от 0 до ꝏ').split())
logging.info('Введены значения a, b')
try:
    if a > 0 and b > 0:
        print(random_numbers(a, b))
        logging.info('Генерируем рандомное число и выводим его')
    else:
        logging.error('Недопустимые границы диапазона')
        raise Exception('Error: Введите диапазон значений заново') 
except Exception as e:
    print(e)






# import random
# import logging

# logging.basicConfig(level=logging.DEBUG)  #, filename="py_log.log",filemode="w")

# def random_numbers(a, b):
#     try:
#        if a > 0 and b > 0:
#             logging.info('a > 0 и b > 0')
#             num = random.randint(a, b)
#             logging.info('Генерируем рандомное число')
#             return num
#        else:
#             logging.error('a < 0 или b < 0')
#             raise Exception('Error: Недопустимые границы диапазона. Введите диапазон значений заново')
       
#     except Exception as e:
#         logging.info('Возвращаем значение ошибки')
#         return 'Error: ' + str(e)


# a, b = map(float, input(f'Введите диспазон чисел от 0 до ꝏ').split())
# logging.info('Введены значения a, b')
# print(random_numbers(a, b))
# logging.info('Выведено случайное число')
