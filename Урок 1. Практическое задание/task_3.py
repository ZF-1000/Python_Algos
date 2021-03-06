"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой, проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

# y = kx + b - общий вид уравнения
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
while True:
    try:
        print('Введите координаты точки А (X1_VAL; Y1_VAL):')
        X1_VAL = float(input('\tX1_VAL = '))
        Y1_VAL = float(input('\tY1_VAL = '))

        print('Введите координаты точки B (X2_VAL; Y2_VAL):')
        X2_VAL = float(input('\tX2_VAL = '))
        Y2_VAL = float(input('\tY2_VAL = '))

        print('Уравнение прямой, проходящей через эти точки: ')
        K = (Y1_VAL - Y2_VAL) / (X1_VAL - X2_VAL)
        B = Y2_VAL - K * X2_VAL
        print(f'y = {round(K, 3)} * x + {round(B, 3)}')
        break
    except ValueError:
        print('Некорректно введённые данные!\n')
