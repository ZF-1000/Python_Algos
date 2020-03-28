"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""


for i in range(2, 10):
    flag = 0
    for j in range(2, 100):
        if j % i == 0:
            flag += 1
    print(f'В диапазоне [2-99]: {flag} чисел кратны \'{i}\'')



# # Вариант №2 через функцию
# def cycle_method(from_n, to_n, from_r, to_r, output_str=''):
#     for i in range(from_n, to_n + 1):
#         flag = 0
#         for j in range(from_r, to_r + 1):
#             if j % i == 0:
#                 flag += 1
#         output_str += f'В диапазоне [{from_r}-{to_r}]: {flag} чисел кратны \'{i}\'\n'
#     return output_str
#
#
# from_numb = 2
# to_numb = 9
# from_range = 2
# to_range = 99
#
# print(cycle_method(from_numb, to_numb, from_range, to_range))


# # Вариант №2 через рекурсию
# def recur_method(from_n, to_n, from_r, to_r, output_str=''):
#     for i in range(from_n, to_n + 1):
#         flag = 0
#         for j in range(from_r, to_r + 1):
#             if j % i == 0:
#                 flag += 1
#         output_str += f'В диапазоне [{from_r}-{to_r}]: {flag} чисел кратны \'{i}\'\n'
#     print(output_str)
#     if from_n > to_n:
#         return recur_method(from_n, to_n, from_r, to_r)
#
#
# from_numb = 2
# to_numb = 9
# from_range = 2
# to_range = 99
#
# print(recur_method(from_numb, to_numb, from_range, to_range))
