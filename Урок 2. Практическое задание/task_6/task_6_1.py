"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

import random

NUMBER = random.randint(0, 100)
# print(NUMBER) # для отладки

USER_NUMBER = None
COUNT = 0  # счётчик числа попыток
MAX_COUNT = 10  # максимальное число попыток
IS_WINNER = False

while not IS_WINNER:
    COUNT += 1  # подсчет числа попыток
    if COUNT > MAX_COUNT:
        print(f'Вы проиграли, загаданное число: "{NUMBER}"')
        break

    print(f'\nПопытка № {COUNT}')
    while True:
        try:
            USER_NUMBER = int(input('Введите число от 0 до 100: '))
            if USER_NUMBER == NUMBER:
                IS_WINNER = True
                print(
                    f'Вы победили! Загаданное число действительно "{NUMBER}"')
                break
            if NUMBER < USER_NUMBER:
                print('Ваше число больше загаданного')
                break
            print('Ваше число меньше загаданного')
            break
        except ValueError:
            print('Некорректно введены данные!\n')
