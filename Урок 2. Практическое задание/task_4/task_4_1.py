"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

while True:
    try:
        COUNT = int(input('Введите количество элементов: '))
        NUMBER = 1
        i = 0
        SUM = 0
        LIST_NUMBER = []
        while i != COUNT:
            SUM += NUMBER
            LIST_NUMBER.append(NUMBER)
            NUMBER = NUMBER / (-2)
            i += 1

        print(f'Элементы ряда: {LIST_NUMBER}')
        print(f'Количество элементов: {COUNT}, их сумма: {SUM} ')
        break
    except ValueError:
        print('Некорректно введены данные!\n')
