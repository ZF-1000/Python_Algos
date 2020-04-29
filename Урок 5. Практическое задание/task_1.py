"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

import collections
from collections import namedtuple

# Вариант №1. Решение через "namedtuple"
LST = []
NUMB_COMPANY = int(
    input('Введите количество предприятий для расчета прибыли: '))
for i in range(NUMB_COMPANY):
    name_company = input(f'Введите название {i + 1}-го предприятия: ')
    PROFIT_COMPANY = list(map(int, input(
        'Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ').split()))

    company = namedtuple('company', 'name_company PROFIT_COMPANY')
    comp = company(name_company, PROFIT_COMPANY)
    LST.append(comp)  # полный кортеж всех компаний

COMP_TUPLE = []
for i in range(NUMB_COMPANY):
    COMP_TUPLE.append(LST[i].name_company)  # кортеж предприятий

PROFIT_TUPLE = []
for i in range(NUMB_COMPANY):
    # кортеж списков с прибылью предприятий
    PROFIT_TUPLE.append(LST[i].PROFIT_COMPANY)

TOTAL_PROFIT = 0
ITER = len(PROFIT_TUPLE)
for i in range(ITER):
    # суммарная прибыль за год по всем предприятиям
    TOTAL_PROFIT += sum(PROFIT_TUPLE[i])

AVG_PROFIT = TOTAL_PROFIT / NUMB_COMPANY
print(f'\nСредняя годовая прибыль всех предприятий: {AVG_PROFIT}')

# список годовых доходов предприятий
PROFIT_COMPANY = list(map(sum, PROFIT_TUPLE))

# предприятия которые имеют прибыль выше среднего значения (или равную)
# выводим в первую очередь
BIG_COMPANY = []
BIG_PROFIT = []
LITTLE_COMPANY = []
LITTLE_PROFIT = []
ITER = len(PROFIT_COMPANY)
for i in range(ITER):
    if PROFIT_COMPANY[i] >= AVG_PROFIT:
        BIG_COMPANY.append(COMP_TUPLE[i])
        BIG_PROFIT.append(PROFIT_COMPANY[i])
    else:
        LITTLE_COMPANY.append(COMP_TUPLE[i])
        LITTLE_PROFIT.append(PROFIT_COMPANY[i])
print(f'Предприятия, с прибылью выше среднего значения: {BIG_COMPANY}')

# **Добавил для наглядности (можно убрать)
print('Годовая прибыль предприятий:')
ITER = len(BIG_COMPANY)
for i in range(ITER):  # **
    print(f'{BIG_COMPANY[i]} - {BIG_PROFIT[i]}')  # **

print(f'Предприятия, с прибылью ниже среднего значения: {LITTLE_COMPANY}')

print('Годовая прибыль предприятий:')  # **
ITER = len(LITTLE_COMPANY)
for i in range(ITER):  # **
    print(f'{LITTLE_COMPANY[i]} - {LITTLE_PROFIT[i]}')  # **

# Вариант №2. Решение через "defaultdict"
print('\n========================================================================================')

NUMB_COMPANY = int(
    input('Введите количество предприятий для расчета прибыли: '))

COMP = collections.defaultdict(list)

for i in range(NUMB_COMPANY):
    name_company = input(f'Введите название {i + 1}-го предприятия: ')
    PROFIT_COMPANY = list(map(int, input(
        'Через пробел введите прибыль данного предприятия за каждый квартал (всего 4 квартала): ').split()))
    COMP[name_company] = sum(PROFIT_COMPANY)

AVG_PROFIT = sum(COMP.values()) / NUMB_COMPANY
print(f'\nСредняя годовая прибыль всех предприятий: {AVG_PROFIT}')

BIG_COMPANY = []
LITTLE_COMPANY = []
for i in COMP:
    if COMP[i] >= AVG_PROFIT:
        BIG_COMPANY.append(i)
    else:
        LITTLE_COMPANY.append(i)

print(f'Предприятия, с прибылью выше среднего значения: {BIG_COMPANY}')
print(f'Предприятия, с прибылью ниже среднего значения: {LITTLE_COMPANY}')
