#Дана сторона квадрата a. Найти его периметр P = 4·a
a = float(input())
P = 4*a
print(P)

#Дан сторона квадрата a. Найти его площадь{{ S = a2}}
a = float(input())
S = a**2
print(S)

#Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
a, b = map(float, input().split())
S = a*b
print(S)

#Дан диаметр окружности d. Найти ее длину{{ L = π·d, π = 3.14}}
import math
d = float(input())
L = round(math.pi*d, 2)
print(L)

#Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
a = float(input())
V = a**3
S = 6*a**2
print(V, S)

#Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
a, b, c = map(float, input().split())
V = a*b*c 
S = 2*(a*b + b*c + a*c)
print(V, S)

#Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
import math
R = float(input())
L = 2*math.pi*R
S = math.pi*R**2
print(L, S)

#Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
a, b = map(float, input().split())
srA = (a + b)/2
print(srA)

#Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a·b)1/2
a, b = map(float, input().split())
srG = (a*b)**0.5
print(srG)

#Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
a, b = [float(x)**2 for x in input().split()]
summ = round(a+b, 2)
deduct = round(a-b, 2)
product = round(a*b, 2)
quotient = round(a/b, 2)
print(summ, deduct, product, quotient)
