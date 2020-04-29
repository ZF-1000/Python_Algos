"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.

Пример:
строка: рара

подстроки:
рар
ра
р
а
ар
ара

Итог: 6 подстрок
"""

import hashlib


STR = input("Введите строку из маленьких латинских букв: ")
hash_set = set()

LENGTH_STR = len(STR)
for i in range(LENGTH_STR):
    if i == 0:
        LENGTH_STR = len(STR) - 1
    else:
        LENGTH_STR = len(STR)
    for j in range(LENGTH_STR, i, -1):
        length_data_set = len(hash_set)
        hash_set.add(hashlib.sha1(STR[i:j].encode('utf-8')).hexdigest())

        if length_data_set != len(hash_set):
            print(STR[i:j])
print(hash_set)


print(f'Количество различных подстрок в строке "{STR}" равно {len(hash_set)}')
