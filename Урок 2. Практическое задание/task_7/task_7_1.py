"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    try:
        NUMBER = int(input('Введите n: '))
        SUM = 0
        for i in range(1, NUMBER + 1):
            SUM += i
        TOTAL = NUMBER * (NUMBER + 1) // 2
        print(f'1 + 2 + ... + n = {SUM}')
        print(f'n * (n + 1) / 2 = {SUM}')
        if SUM == TOTAL:
            print('Равенство 1+2+...+n = n(n+1)/2 выполняется!')
            break
        print('Что-то пошло не так')
        break
    except ValueError:
        print('Некорректно введены данные!\n')
