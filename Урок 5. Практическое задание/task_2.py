"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

import collections
from functools import reduce
from collections import deque

print('\n========================================================================================')
print('Вариант №1. Решение через "defaultdict"'.center(80))

NUMBS = collections.defaultdict(list)


def sum_hex():
    '''"""defaultdict"""'''
    print('Сумма чисел')
    for i in range(2):
        j = input(f'Введите {i + 1}-е шестнадцатиричное число: ')
        NUMBS[i] = list(j)

    numb_1 = ''.join(NUMBS[0])  # 1-е шестнадцатиричное число
    numb_2 = ''.join(NUMBS[1])  # 2-е шестнадцатиричное число
    # NUMBS.values() - список значений словаря в виде списка [['A', 'A'],
    # ['B', 'B', 'B']]
    # перевёл значения словаря в десятичную систему счисления
    decimal_numb = [int(''.join(n), 16) for n in NUMBS.values()]
    hex_numb = hex(sum(decimal_numb)).upper()
    # hex_numb[2:] - отбрасываем '0x'
    print(f"{numb_1.upper()} + {numb_2.upper()} = {hex_numb[2:]}")


sum_hex()


def mult_hex():
    '''defaultdict'''
    print('\nПроизведение чисел')
    for i in range(2):
        j = input(f'Введите {i + 1}-е шестнадцатиричное число: ')
        NUMBS[i] = list(j)

    numb_1 = ''.join(NUMBS[0])
    numb_2 = ''.join(NUMBS[1])

    decimal_numb = [int(''.join(n), 16) for n in NUMBS.values()]
    hex_numb = hex(decimal_numb[0] * decimal_numb[1]).upper()
    print(f"{numb_1.upper()} * {numb_2.upper()} = {hex_numb[2:]}")


mult_hex()


print('\n========================================================================================')
print('Вариант №2. Решение через "deque"'.center(80))


def sum_hex_var2(numb_1, numb_2):
    """deque"""
    print('Сумма чисел')
    hex_lst = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    lst_1 = deque(numb_1)
    lst_2 = deque(numb_2)

    result = deque()
    flag = 0
    if len(lst_2) > len(lst_1):
        lst_1, lst_2 = deque(numb_2), deque(numb_1)  # теперь lst_1 > lst_2

    while lst_1:  # пока lst_1 не станет пустым списком
        if lst_2:  # пока lst_2 не станет пустым списком
            # складвыем по последней позиции из lst_1 и lst_2
            res = hex_lst[lst_1.pop()] + hex_lst[lst_2.pop()] + flag
        else:
            res = hex_lst[lst_1.pop()] + flag
        flag = 0
        if res < 16:
            result.appendleft(hex_lst[res])
        else:
            result.appendleft(hex_lst[res - 16])
            flag = 1
    if flag:
        result.appendleft('1')

    print(f'{list(numb_1)} + {list(numb_2)} = {list(result)}')


print('\n')

NUMB_A = input(f'Введите 1-е шестнадцатиричное число: ').upper()
NUMB_B = input(f'Введите 2-е шестнадцатиричное число: ').upper()

sum_hex_var2(NUMB_A, NUMB_B)


def mult_hex_var2(numb_1, numb_2):
    """deque"""
    print('Произведение чисел')
    hex_lst = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    numbs = collections.defaultdict(list)

    lst_1 = deque(numb_1)
    lst_2 = deque(numb_2)

    result = deque()

    if len(lst_2) > len(lst_1):
        lst_1, lst_2 = deque(numb_2), deque(numb_1)  # теперь lst_1 > lst_2

    for j in range(len(lst_2)):             # ** блок операции умножения
        flag = 0
        for i in range(len(lst_1)):
            res = hex_lst[lst_1[-1 - i]] * hex_lst[lst_2[-1 - j]] + flag
            flag = res // 16  # целая часть (переносим на следующий порядок)
            res = res % 16  # остаток от деления
            result.appendleft(hex_lst[res])
        if flag:  # если после последней операции умножения есть изменение порядка
            # добавляем последний flag к результату
            result.appendleft(hex_lst[flag])
        # numbs - словарь defaultdict. Где ключ - это порядки, а значения - это
        # результаты умножения по порядкам
        numbs[j] = list(result)
        result = deque()                    # **

    # Что бы сложить значения, получившиеся после операций перемножения надо
    # учесть порядок списков для сложения
    align_lst = deque()
    itr = len(numbs)
    for i in range(itr):
        align_lst.append(['0'] * (len(numbs) - i - 1) + numbs[i] + ['0'] * i)
        # добавили '0' в начало для первый порядков и '0' в конец для последних порядков
        # теперь списки готовы к сложению по элементно с учётом порядков
        # списков
    flag = 0                            # *** блок операции сложения
    while align_lst[0]:
        j = []
        for i in align_lst:
            j.append(hex_lst[i.pop()])
        # print(j)
        summ = reduce(lambda x, y: x + y, j)
        summ = summ + flag
        flag = 0
        if summ < 16:
            result.appendleft(hex_lst[summ])
        else:
            result.appendleft(hex_lst[summ % 16])
            flag = summ // 16           # # ***

    print(f'{list(numb_1)} * {list(numb_2)} = {list(result)}')


mult_hex_var2(NUMB_A, NUMB_B)


print('\n========================================================================================')
print('Вариант №3. Решение с помощью ООП'.center(80))


class HexNumber:
    """Перегрузка методов"""
    def __init__(self, hex_num):
        self.number = list(hex_num)

    def __str__(self):
        return self.number.__str__()

    def __add__(self, other):
        # сообщаем, что число находится в 16-ой системе счисления и возвращаем
        # его значение в 10-ой системе счисления
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 + numb_2)[2:].upper()}')

    def __mul__(self, other):
        numb_1 = int(''.join(self.number), 16)
        numb_2 = int(''.join(other.number), 16)
        return HexNumber(f'{hex(numb_1 * numb_2)[2:].upper()}')


NUMB_A = input(f'Введите 1-е шестнадцатиричное число: ').upper()
NUMB_B = input(f'Введите 2-е шестнадцатиричное число: ').upper()
HEX_NUMB_1 = HexNumber(NUMB_A)
HEX_NUMB_2 = HexNumber(NUMB_B)
print(f'{list(NUMB_A)} + {list(NUMB_B)} = {HEX_NUMB_1 + HEX_NUMB_2}')
print(f'{list(NUMB_A)} * {list(NUMB_B)} = {HEX_NUMB_1 * HEX_NUMB_2}')
