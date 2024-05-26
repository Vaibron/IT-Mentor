"""
Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton
"""


class Dog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return "Гав!"

    def describe(self):
        return f"{self.name} это {self.breed} и ему {self.age} лет."


# Пример использования
dog1 = Dog("Оппи", "Лабрадор", 3)
dog2 = Dog("Феня", "Мопс", 5)

print(dog1.describe())  # Выведет: Феня это Мопс и ему 5 лет.
print(dog2.describe())  # Феня это Мопс и ему 5 лет.

print(dog1 is dog2)  # Выведет: True, так как это Singleton
