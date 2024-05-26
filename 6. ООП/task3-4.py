"""
3) Создайте класс {{MeansOfTransport }}(для определения цвета и марки машины),
принимающий 2 аргумента при инициализации (марка и цвет транспортного средства).
В этом классе реализуйте методы show_color(),
выводящий на печать цвет транспортного средства и show_brand,
для получения марки транспортного средства.

4) Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
"""


class MeansOfTransport:
    def __init__(self, brand, color):
        self._brand = brand
        self._color = color

    def show_color(self):
        print("Цвет транспортного средства:", self._color)

    def show_brand(self):
        return self._brand

    # Геттер для цвета
    def get_color(self):
        return self._color

    # Сеттер для цвета
    def set_color(self, color):
        self._color = color

    # Геттер для марки
    def get_brand(self):
        return self._brand

    # Сеттер для марки
    def set_brand(self, brand):
        self._brand = brand


# Пример использования класса
vehicle = MeansOfTransport("Toyota", "Красная")
vehicle.show_color()  # Выведет: Цвет транспортного средства: Красная
print("Марка транспортного средства:", vehicle.show_brand())  # Выведет: Марка транспортного средства: Toyota

# Использование геттеров и сеттеров
print("Текущий цвет транспортного средства:", vehicle.get_color())  # Выведет: Текущий цвет транспортного средства: Красная
vehicle.set_color("Синяя")
print("Новый цвет автомобиля:", vehicle.get_color())  # Выведет: Новый цвет автомобиля: Синяя

print("Текущая марка транспортного средства:",
      vehicle.get_brand())  # Выведет: Текущая марка транспортного средства: Toyota
vehicle.set_brand("Honda")
print("Новая марка транспортного средства:", vehicle.get_brand())  # Выведет: Новая марка транспортного средства: Honda
