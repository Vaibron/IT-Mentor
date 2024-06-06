'''Напишите класс, который принимает список людей с интерфейсом добавления новых
и при итерации возвращал имена людей'''


class PeopleList:
    def __init__(self):
        self.lst = []

    def add_person(self, name):
        self.lst.append(name)

    def __iter__(self):
        self.flag = 0
        return self

    def __next__(self):
        if self.flag < len(self.lst):
            county = self.lst[self.flag]
            self.flag += 1
            return county
        else:
            raise StopIteration

    def iterate_class(self):
        for person in self:
            print(person)


people_list = PeopleList()
people_list.add_person("Елизавета")
people_list.add_person("Алексей")
people_list.add_person("Роберт Оппенгеймер")

people_list.iterate_class()
