import logging

logging.basicConfig(
    level=logging.INFO,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


class LoggedAttributes:
    def __init__(self, atr1, atr2, atr3):
        self.atr1 = atr1
        self.atr2 = atr2
        self.atr3 = atr3

    @property
    def attr1(self):
        return self.atr1

    @attr1.setter
    def attr1(self, value):
        logging.info(f'atr1 изменен с {self.atr1} на {value}')
        self.atr1 = value

    @property
    def attr2(self):
        return self.atr2

    @attr2.setter
    def attr2(self, value):
        logging.info(f'atr2 изменен с {self.atr2} на {value}')
        self.atr2 = value

    @property
    def attr3(self):
        return self.atr3

    @attr3.setter
    def attr3(self, value):
        logging.info(f'atr3 изменен с {self.atr3} на {value}')
        self.atr3 = value


# Пример использования:
obj = LoggedAttributes('Один', 'Два', 'Три')
obj.attr1 = 'Четыре'
obj.attr2 = 'Пять'
obj.attr3 = 'Шесть'

# class LoggedAttributes:
#     def __init__(self, atr1, atr2, atr3):
#         self.atr1 = atr1
#         self.atr2 = atr2
#         self.atr3 = atr3
#
#     def __setattr__(self, name, value):
#         if name in ['atr1', 'atr2', 'atr3']:
#             old_value = getattr(self, name, None)
#             if old_value != value:
#                 logging.info(f'{name} изменен с {old_value} на {value}')
#         super().__setattr__(name, value)
