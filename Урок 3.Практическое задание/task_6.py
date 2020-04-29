"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

Подсказки:
1) берем первый минимальный и максимальный
2) не забудьте, что сначала может быть минимальный, потом максимальный
а может - наоборот. во всех этих случаях нужна корректная работа

Пример:
Введите количество элементов в массиве: 10
Массив: [88, 58, 50, 77, 49, 6, 42, 67, 14, 79]
Сумма элементов между минимальным (6)  и максимальным (88) элементами: 234
"""

from random import random

while True:
    try:
        # число элементов в массиве
        N = int(input('\nВведите количество элементов в массиве: '))
        NUMS_LST = [0] * N
        for i in range(N):
            # заполняем массив числами [0,99]
            NUMS_LST[i] = int(random() * 100)
        print(f'Исходный массив:\n{NUMS_LST}')

        INDEX_MIN_NUMS = NUMS_LST.index(min(NUMS_LST))
        INDEX_MAX_NUMS = NUMS_LST.index(max(NUMS_LST))
        print('\nСписок <<индекс:начение>>')
        for i, v in enumerate(NUMS_LST, 0):
            print(f'{i}:{v}', end='  ')

        print(f'\n\nИндекс минимального элемента: {INDEX_MIN_NUMS}')
        print(f'Индекс максимального элемента: {INDEX_MAX_NUMS}')
        TOTAL_NUMS = 0
        if INDEX_MAX_NUMS < INDEX_MIN_NUMS:
            for i in range(INDEX_MAX_NUMS + 1, INDEX_MIN_NUMS):
                TOTAL_NUMS = TOTAL_NUMS + NUMS_LST[i]
        else:
            for i in range(INDEX_MIN_NUMS + 1, INDEX_MAX_NUMS):
                TOTAL_NUMS = TOTAL_NUMS + NUMS_LST[i]
        print(
            f'Сумма элементов между минимальным \'{NUMS_LST[INDEX_MIN_NUMS]}\'',
            end=' ')
        print(
            f'и максимальным \'{NUMS_LST[INDEX_MAX_NUMS]}\' элементами: {TOTAL_NUMS}')
        break
    except ValueError:
        print('Некорректно введённые данные!')
