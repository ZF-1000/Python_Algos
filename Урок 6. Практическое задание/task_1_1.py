# _________________Анализ использования слотов в классах_________________

"""
Реализация №1. Без использования слотов
"""

from pympler import asizeof


class HexNumber:
    """Перегрузка методов"""
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 + numb_2)[2:].upper()}')

    def __mul__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 * numb_2)[2:].upper()}')


HEX_NUMB_1 = HexNumber('A2')
HEX_NUMB_2 = HexNumber('C4F')
print(f'{list(HEX_NUMB_1.number)} + {list(HEX_NUMB_2.number)} = {HEX_NUMB_1 + HEX_NUMB_2}')
print(f'{list(HEX_NUMB_1.number)} * {list(HEX_NUMB_2.number)} = {HEX_NUMB_1 * HEX_NUMB_2}')

print(f'Объект: "{HEX_NUMB_1.__dict__}"\tРазмер: {asizeof.asizeof(HEX_NUMB_1)}')
print(f'Объект: "{HEX_NUMB_2.__dict__}"\tРазмер: {asizeof.asizeof(HEX_NUMB_2)}\n')


"""
Реализация №2. С использованием слотов
"""


class HexNumber:
    __slots__ = 'number'
    """Перегрузка методов"""
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 + numb_2)[2:].upper()}')

    def __mul__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 * numb_2)[2:].upper()}')


HEX_NUMB_1 = HexNumber('A2')
HEX_NUMB_2 = HexNumber('C4F')

print(f'{list(HEX_NUMB_1.number)} + {list(HEX_NUMB_2.number)} = {HEX_NUMB_1 + HEX_NUMB_2}')
print(f'{list(HEX_NUMB_1.number)} * {list(HEX_NUMB_2.number)} = {HEX_NUMB_1 * HEX_NUMB_2}')

print(f'Объект: "{HEX_NUMB_1.number}"\tРазмер: {asizeof.asizeof(HEX_NUMB_1)}')
print(f'Объект: "{HEX_NUMB_2.number}"\tРазмер: {asizeof.asizeof(HEX_NUMB_2)}')


# ['A', '2'] + ['C', '4', 'F'] = CF1
# ['A', '2'] * ['C', '4', 'F'] = 7C9FE
# Объект: "{'number': 'A2'}"	Размер: 168
# Объект: "{'number': 'C4F'}"	Размер: 168
#
# ['A', '2'] + ['C', '4', 'F'] = CF1
# ['A', '2'] * ['C', '4', 'F'] = 7C9FE
# Объект: "A2"	Размер: 32
# Объект: "C4F"	Размер: 32

'''
Использование __slots__ действительно может увеличить производительность,
особенно уменьшив количество используемой памяти при создании множества небольших объектов.
Из примера выше использование __slots__ позволяет в 5,2 раза съэкономить место.
__slots__ предполагают отказ от словарей, а ведь под словари выделяется значительно больше памяти, чем нужно,
однако надо помнить, что __slots__ требуют явного указания параметров (динамически их добавить не получится)
'''