"""Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. 
Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими
коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции."""

import logging

logging.basicConfig(filename="py_log2.log")


def quadratic_equation(a, b, c):
    D = b ** 2 - 4 * a * c
    try:
        if D > 0:
            x1 = (-b - D ** 0.5) / (2 * a)
            x2 = (-b + D ** 0.5) / (2 * a)
            return x1, x2
        elif D == 0:
            logging.warning('D = 0')
            x = -b / 2 * a
            return x
        else:
            raise Exception('D < 0')

    except Exception as e:
        logging.error(e)
        return str('Попробуйте еще раз с другими коэффициентами')


try:
    a, b, c = map(float, input('Введите коэффициенты уравнения: a, b, c: ').split())
    print(quadratic_equation(a, b, c))
except Exception as e:
    logging.error(e)
    print('Попробуйте еще раз с другими коэффициентами')
