"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
while True:
    try:
        AMOUNT_NUMB = int(input('Сколько будет чисел? - '))
        NUMBER = int(input('Какую цифру считать? - '))
        COUNT = 0
        for i in range(1, AMOUNT_NUMB + 1):
            m = int(input(f'Число {str(i)}: '))
            while m > 0:
                if m % 10 == NUMBER:  # сравниваем последнюю цифру числа с NUMBER
                    COUNT += 1  # счётчик
                m = m // 10  # убираем последнюю цифру в числе

        print(f'Было введено {COUNT} цифр(ы) "{NUMBER}"')
        break
    except ValueError:
        print('Некорректно введены данные!\n')
