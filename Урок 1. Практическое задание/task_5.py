"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""

# Вариант №1
while True:
    try:
        print('\n=== Индексы введённых букв и количество позиций между ними ===')
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
        print(f'Буква \'{LEFT_CHAR}\' имеет индекс: {INDEX_LEFT_CHAR + 1}')
        print(f'Буква \'{RIGHT_CHAR}\' имеет индекс: {INDEX_RIGHT_CHAR + 1}')
        if INDEX_RIGHT_CHAR > INDEX_LEFT_CHAR:
            print(
                f'Выбранный диапазон: {ALPH[INDEX_LEFT_CHAR: (INDEX_RIGHT_CHAR + 1)]}')
        else:
            print(
                f'Выбранный диапазон: {ALPH[INDEX_RIGHT_CHAR: (INDEX_LEFT_CHAR + 1)]}')
        print(
            f'Между введёнными буквами: {abs(INDEX_RIGHT_CHAR - INDEX_LEFT_CHAR) - 1} букв(ы)')
        break
    except ValueError:
        print('Некорректно введённые данные!\n')

# Вариант №2
while True:
    try:
        print('\n=== Индексы введённых букв и количество позиций между ними (Вариант №2) ===')
        LEFT_CHAR = input('Введите первую букву диапазона: ')
        RIGHT_CHAR = input('Введите вторую букву диапазона: ')

        LEFT_CHAR = LEFT_CHAR.lower()
        RIGHT_CHAR = RIGHT_CHAR.lower()

        if ('a' <= LEFT_CHAR <= 'z') and ('a' <= RIGHT_CHAR <= 'z'):
            INDEX_LEFT_CHAR = ord(LEFT_CHAR)
            INDEX_RIGHT_CHAR = ord(RIGHT_CHAR)
            print(
                f'Буква \'{LEFT_CHAR}\' в алфавите имеет индекс: {INDEX_LEFT_CHAR - 96}')
            print(
                f'Буква \'{RIGHT_CHAR}\' в алфавите имеет индекс: {INDEX_RIGHT_CHAR - 96}')

            print(
                f'Между введёнными буквами: {abs(INDEX_RIGHT_CHAR - INDEX_LEFT_CHAR) - 1} букв(ы)')
            break
        print('Введите букву в диапазоне от a до z\n')
    except ValueError:
        print('Некорректно введённые данные!\n')
