"""
Закодируйте любую строку из трех слов по алгоритму Хаффмана.

Пример:
строка для кодирования
s = "beep boop beer!"

Результат:
00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001
"""


from collections import Counter, deque


def huffman_tree(s):
    uniq_char = Counter(s)          # считаем уникальные символы
    sorted_el = deque(sorted(uniq_char.items(), key=lambda item: item[1]))  # сортируем по возр. кол-ва повторений
    if len(sorted_el) != 1:           # проверка, если строка состоит из одного повторяющего символа
        while len(sorted_el) > 1:     # цикл для построения дерева (объединяем два крайних левых элемента)
            frequence = sorted_el[0][1] + sorted_el[1][1]  # вес объединенного элемента (накопленная частота)
            comb = {0: sorted_el.popleft()[0],    # объединенный элемент
                    1: sorted_el.popleft()[0]}
            for i, _count in enumerate(sorted_el):    # место для ставки объединенного элемента
                if frequence > _count[1]:
                    continue
                else:
                    sorted_el.insert(i, (comb, frequence))   # вставляем объединенный элемент
                    break
            else:
                sorted_el.append((comb, frequence))      # добавляем объединенный корневой элемент
    else:
        frequence = sorted_el[0][1]      # приравниваемыем значение 0 к одному повторяющемуся символу
        comb = {0: sorted_el.popleft()[0], 1: None}
        sorted_el.append((comb, frequence))
    return sorted_el[0][0]        # словарь - дерево


code_table = dict()


def huffman_code(tree, path=''):
    if not isinstance(tree, dict):  # если элемент не словарь, значит мы достигли самого символа
        code_table[tree] = path     # заносим элемент, а так же его код в словарь (кодовую таблицу)
    else:       # если элемент словарь, рекурсивно спускаемся вниз по первому и второму значению
        huffman_code(tree[0], path=f'{path}0')      # левая ветвь
        huffman_code(tree[1], path=f'{path}1')      # правая ветвь


str = "beep boop beer!"       # строка для кодирования


huffman_code(huffman_tree(str))   # функция заполняет кодовую таблицу (символ-его код)

print(f'\nСтрока для кодирования:\n{str}')
print('\nРезультат кодировки:')
for i in str:
    print(code_table[i], end=' ')   # выводим коды для каждого символа
print()
