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


dog1 = Dog("Оппи", "Метис", 3)
dog2 = Dog("Феня", "Мопс", 5)

print(dog1.describe())
print(dog2.describe())

print(dog1 is dog2)
