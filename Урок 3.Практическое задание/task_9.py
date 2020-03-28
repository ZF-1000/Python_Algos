"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""

from random import random

i = int(input('Задайте количество строк в матрице: '))
j = int(input('Задайте количество столбцов в матрице: '))

ARRAY = []
for r in range(i):
    NUMB_LST = []
    for n in range(j):
        k = int(random() * 100)  # максимальный элемент массива 99
        NUMB_LST.append(k)
    print(NUMB_LST)
    ARRAY.append(NUMB_LST)  # сформировали матрицу i х j

MIN_LST = []
for c in range(j):
    min_elem = 100
    for r in range(i):
        if ARRAY[r][c] < min_elem:
            min_elem = ARRAY[r][c]
    MIN_LST.append(min_elem)
print(f'{MIN_LST} - минимальные значения по столбцам')
print(f'Максимальное среди них = {max(MIN_LST)}')
