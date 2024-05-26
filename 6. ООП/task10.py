"""
10) Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
Реализуйте еще один класс, который будет наследоваться от класса Calculator
и перегрузите метод для вычисления суммы двух чисел, чтобы он делал конкатенацию двух строк.
"""


class Calculator:
    def add(self, x, y):
        return x + y

class StringConcatenator(Calculator):
    def add(self, x, y):
        return str(x) + str(y)

# Пример использования
calc = Calculator()
result1 = calc.add(3, 5)  # Вычислит сумму чисел: 3 + 5 = 8
print("Результат сложения:", result1)

str_concatenator = StringConcatenator()
result2 = str_concatenator.add("Привет", "Мир")  # Произведет конкатенацию строк: "Привет" + "Мир" = "ПриветМир"
print("Результат объединения строк:", result2)