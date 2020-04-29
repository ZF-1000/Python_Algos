"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""

from random import random

N = 15  # число элементов в массиве
LST = [0] * N
for i in range(N):
    LST[i] = int(random() * 10)  # заполняем массив числами [0,9]
print(LST)

# первый элемент массива с 0-ым числом повторений является максимальным
MAX_NUMB = (0, LST[0])
for element in LST:
    count_numb = LST.count(element)
    if count_numb > MAX_NUMB[0]:
        MAX_NUMB = (count_numb, element)
print(
    f'Чаще всего повторяется \'{MAX_NUMB[1]}\'\nЧисло повторяется {MAX_NUMB[0]} раз(а)')
