"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""


import random


def merge(left_lst, right_lst):  
    sorted_lst = []
    left_lst_index = right_lst_index = 0
    left_lst_len, right_lst_len = len(left_lst), len(right_lst)

    for _ in range(left_lst_len + right_lst_len):
        if left_lst_index < left_lst_len and right_lst_index < right_lst_len:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, 
            # добавляем его в отсортированный массив
            if left_lst[left_lst_index] <= right_lst[right_lst_index]:
                sorted_lst.append(left_lst[left_lst_index])
                left_lst_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_lst.append(right_lst[right_lst_index])
                right_lst_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_lst_index == left_lst_len:
            sorted_lst.append(right_lst[right_lst_index])
            right_lst_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_lst_index == right_lst_len:
            sorted_lst.append(left_lst[left_lst_index])
            left_lst_index += 1

    return sorted_lst



def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2    # Середина списка

    # Сортируем и объединяем подсписки
    # Список рекурсивно разделяем пополам, пока в итоге не получатся списки размеров в один элемент
    left_lst = merge_sort(nums[:center])
    right_lst = merge_sort(nums[center:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_lst, right_lst)


count = int(input('Введите число элементов: '))
random_lst = [random.uniform(0, 50) for _ in range(count)]

print(f'Исходный массив: {random_lst}')
print(f'Отсортированный массив: {merge_sort(random_lst)}')


# Введите число элементов: 5
# Исходный массив: [14.740345998796034, 8.530983835974649, 10.520624760577551, 5.458201953964603, 38.010309770838916]
# Отсортированный массив: [5.458201953964603, 8.530983835974649, 10.520624760577551, 14.740345998796034, 38.010309770838916]
