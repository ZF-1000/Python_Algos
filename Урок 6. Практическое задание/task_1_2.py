# _________________Реализация с помощью применения декораторов_________________

import time
import memory_profiler
from memory_profiler import profile


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(f'Время выполнения функции: {time.perf_counter() - start_time} с')
        return res
    return wrapped


def mem_of_function(function):
    def wrapped(*args):
        m1 = memory_profiler.memory_usage()
        res = function(*args)
        m2 = memory_profiler.memory_usage()
        print(f'Использовано памяти: {m2[0] - m1[0]} Мб')
        return res
    return wrapped


@mem_of_function
@time_of_function
@profile
def prime_numb(fin_numb):
    lst = []
    for k in range(2, fin_numb + 1):
        for i in range(2, k):
            if k % i == 0:
                break
        else:
            lst.append(k)
    return lst


prime_numb(10000)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     27     12.5 MiB     12.5 MiB   @mem_of_function
#     28                             @time_of_function
#     29                             @profile
#     30                             def prime_numb(fin_numb):
#     31     12.5 MiB      0.0 MiB       lst = []
#     32     12.7 MiB      0.0 MiB       for k in range(2, fin_numb + 1):
#     33     12.7 MiB      0.0 MiB           for i in range(2, k):
#     34     12.7 MiB      0.0 MiB               if k % i == 0:
#     35     12.7 MiB      0.0 MiB                   break
#     36                                     else:
#     37     12.7 MiB      0.0 MiB               lst.append(k)
#     38     12.5 MiB      0.0 MiB       return lst
#
#
# Время выполнения функции: 504.38827549200005 с
# Использовано памяти: 0.18359375 Мб


@mem_of_function
@time_of_function
@profile
def prime_numb_ert(fin_numb):
    a = [0] * fin_numb
    for i in range(fin_numb):
        a[i] = i
    a[1] = 0
    m = 2
    while m < fin_numb:
        if a[m] != 0:
            j = m * 2
            while j < fin_numb:
                a[j] = 0
                j = j + m
        m += 1
    lst = []
    for i in a:
        if a[i] != 0:
            lst.append(a[i])
    del a
    return lst


# prime_numb_ert(10000)


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     64     12.5 MiB     12.5 MiB   @mem_of_function
#     65                             @time_of_function
#     66                             @profile
#     67                             def prime_numb_ert(fin_numb):
#     68     12.5 MiB      0.0 MiB       a = [0] * fin_numb
#     69     12.7 MiB      0.0 MiB       for i in range(fin_numb):
#     70     12.7 MiB      0.0 MiB           a[i] = i
#     71     12.7 MiB      0.0 MiB       a[1] = 0
#     72     12.7 MiB      0.0 MiB       m = 2
#     73     12.7 MiB      0.0 MiB       while m < fin_numb:
#     74     12.7 MiB      0.0 MiB           if a[m] != 0:
#     75     12.7 MiB      0.0 MiB               j = m * 2
#     76     12.7 MiB      0.0 MiB               while j < fin_numb:
#     77     12.7 MiB      0.0 MiB                   a[j] = 0
#     78     12.7 MiB      0.0 MiB                   j = j + m
#     79     12.7 MiB      0.0 MiB           m += 1
#     80     12.7 MiB      0.0 MiB       lst = []
#     81     12.7 MiB      0.0 MiB       for i in a:
#     82     12.7 MiB      0.0 MiB           if a[i] != 0:
#     83     12.7 MiB      0.0 MiB               lst.append(a[i])
#     84     12.7 MiB      0.0 MiB       del a
#     85     12.7 MiB      0.0 MiB       return lst
#
#
# Время выполнения функции: 6.6233450519999995 с
# Использовано памяти: 0.33984375 Мб

'''
Рассмотрел просто в качестве тренировки
'''