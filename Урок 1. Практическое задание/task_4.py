"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random

while True:
    try:
        print('=== Случайное целое число из диапазона ===')
        LEFT = int(input("Минимальная граница: "))
        RIGHT = int(input("Максимальная граница: "))
        NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
        print(f'Случайное целое число из выбранного вами диапазона: {NUMB}')

        print('\n=== Случайное вещественное число из диапазона ===')
        LEFT = float(input("Минимальная граница: "))
        RIGHT = float(input("Максимальная граница: "))
        NUMB = random() * (RIGHT - LEFT) + LEFT
        print(
            f'Случайное вещественное число из выбранного вами диапазона: {round(NUMB, 3)}')

        print('\n=== Случайный символ из диапазона ===')
        LEFT_CHAR = input('Введите первую букву диапазона: ')
        RIGHT_CHAR = input('Введите вторую букву диапазона: ')

        LEFT_CHAR = LEFT_CHAR.lower()
        RIGHT_CHAR = RIGHT_CHAR.lower()

        ALPH = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        # индекс элемента в последовательности
        INDEX_LEFT_CHAR = ALPH.index(LEFT_CHAR)
        INDEX_RIGHT_CHAR = ALPH.index(RIGHT_CHAR)
        if INDEX_RIGHT_CHAR > INDEX_LEFT_CHAR:
            print(
                f'Выбранный диапазон: {ALPH[INDEX_LEFT_CHAR: (INDEX_RIGHT_CHAR + 1)]}')
        else:
            print(
                f'Выбранный диапазон: {ALPH[INDEX_RIGHT_CHAR: (INDEX_LEFT_CHAR + 1)]}')
        CHAR = ALPH[int(random() * (INDEX_RIGHT_CHAR -
                                    INDEX_LEFT_CHAR + 1)) + INDEX_LEFT_CHAR]
        print(f'Случайная буква из выбранного вами диапазона: {CHAR}')
        break
    except ValueError:
        print('Некорректно введённые данные!\n')

# Вариант №2

while True:
    try:
        print('\n=== Случайный символ из диапазона (Вариант №2) ===')
        LEFT_CHAR = input('Введите первую букву диапазона: ')
        RIGHT_CHAR = input('Введите вторую букву диапазона: ')

        LEFT_CHAR = LEFT_CHAR.lower()
        RIGHT_CHAR = RIGHT_CHAR.lower()
        if ('a' <= LEFT_CHAR <= 'z') and ('a' <= RIGHT_CHAR <= 'z'):
            INDEX_LEFT_CHAR = ord(LEFT_CHAR)
            INDEX_RIGHT_CHAR = ord(RIGHT_CHAR)

            CHAR = chr(int(random() * (INDEX_RIGHT_CHAR -
                                       INDEX_LEFT_CHAR + 1)) + INDEX_LEFT_CHAR)
            print(f'Случайная буква из выбранного вами диапазона: {CHAR}')
            break
        print('Введите букву в диапазоне от a до z\n')
    except ValueError:
        print('Некорректно введённые данные!\n')
