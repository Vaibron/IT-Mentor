"""
5) Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
При инициализации они должны принимать новый аргументы(количество колес.

6) В классе {{Moped}}напишите статическую функцию,
которая на вход будет принимать расстояние и максимальную скорость,
а на выходе получать время, за которое проедет мопед это расстояние.

7) Попробуйте инициализировать несколько любых переменных в классе Car
и сделайте одну переменную приватной, одну защищенной.
Попробуйте получить к ним доступ. Какой результат?

8) В классе Car добавьте переменную класса car_drive = 4
и реализуйте classmethod, который выводит на экран переменную car_drive

9) Реализуйте все возможные магические методы в классе Car.
"""


class MeansOfTransport:
    def __init__(self, brand, color, num_wheels):
        self._brand = brand
        self._color = color
        self._num_wheels = num_wheels

    def show_color(self):
        print("Цвет транспортного средства:", self._color)

    def show_brand(self):
        return self._brand

    # Геттеры и сеттеры для цвета, марки и количества колес
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_num_wheels(self):
        return self._num_wheels

    def set_num_wheels(self, num_wheels):
        self._num_wheels = num_wheels


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, brand, color, num_wheels, model):
        super().__init__(brand, color, num_wheels)
        self.model = model
        self._private_var = "Это private"
        self.__protected_var = "Это protected"

    @classmethod
    def show_car_drive(cls):
        print("Количество приводов для автомобиля:", cls.car_drive)

    # Магические методы
    def __str__(self):
        return f"Машина: {self.show_brand()} {self.model}, Цвет: {self.get_color()}, Колеса: {self.get_num_wheels()}"

    def __repr__(self):
        return f"Машина({self.show_brand()}, {self.get_color()}, {self.get_num_wheels()}, '{self.model}')"

    def __eq__(self, other):
        return self.show_brand() == other.show_brand() and self.model == other.model

    def __lt__(self, other):
        return self.get_num_wheels() < other.get_num_wheels()

    def __le__(self, other):
        return self.get_num_wheels() <= other.get_num_wheels()


class Moped(MeansOfTransport):
    def __init__(self, brand, color, num_wheels, model):
        super().__init__(brand, color, num_wheels)
        self.model = model

    @staticmethod
    def calculate_time(distance, max_speed):
        time = distance / max_speed
        return time


# Пример использования классов
car1 = Car("Toyota", "Красная", 4, "Camry")
car2 = Car("Honda", "Синяя", 4, "Accord")
moped = Moped("Vespa", "Желтая", 2, "Sprint")

print(car1)  # Выведет: Car: Toyota Camry, Color: Красная, Wheels: 4

print("Доступ к приватной переменной в автомобиле:",
      car1._private_var)  # Выведет: Доступ к приватной переменной в автомобиле: Это private
# print("Доступ к защищенной переменной в автомобиле:", car1.__protected_var)  # Ошибка: AttributeError

Car.show_car_drive()  # Выведет: Количество приводов для автомобиля: 4

print("Время путешествовать на мопеде:", Moped.calculate_time(50, 30))
# Выведет: Время путешествовать на мопеде: 1.6666666666666667
