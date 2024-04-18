"""Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0. 
Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю попробовать еще раз с другими
коэффициентами. При выполнении скрипта в лог должна записываться информация о успехе или неудаче операции."""
import logging
logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w")

def quadratic_equation(a, b, c):
    D = b**2-4*a*c
    logging.info('Узнаем значения D')
    try:
       if D > 0:
            logging.info('D > 0')
            x1 = (-b - D**0.5) / (2*a)
            x2 = (-b + D**0.5) / (2*a)
            logging.info('Возвращаем значения x1 и x2')
            return x1, x2
       elif D == 0:
            logging.info('D = 0')
            x = -b / 2*a
            logging.info('Возвращаем значения x')
            return x
       else:
            logging.error('Исключение: D < 0')
            raise Exception('Попробуйте еще раз с другими коэффициентами')
       
    except Exception as e:
        logging.info('Возвращаем значение ошибки')
        return str(e)


a, b, c = map(float, input().split())
logging.info('Введены значения a, b, c')
print(quadratic_equation(a, b, c))
logging.info('Выводим значение')
