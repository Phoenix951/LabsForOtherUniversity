# программа для создания массива с использованием модуля numpy
import numpy as np

# вводная
print("""
    Для того чтобы получить массив, элементы которого уменьшаются на единицу введите значения:
    m >= n
    Для того чтобы получить массив, элементы которого увеличиваются на единицу введите значения:
    m < n
    """)

# вводим значения n и m
num_m = int(input("Введите значение m: "))
num_n = int(input("Введите значение n: "))

# переменные
num_more_diag = num_m
num_less_diag = num_m
new_num = num_less_diag

# заполнение массива нулевыми элементами и единичной диагональю
mas = np.identity(num_n, dtype=int)

# если m < n, то выводится массив с элементами m+1 и так далее относительно главной диагонали
if num_m < num_n:
    for i in range(len(mas)):
        for j in range(len(mas)):
            if j > i:
                num_m += 1
                mas[i][j] = num_m
            if j < i:
                mas[i][j] = new_num
                new_num -= 1
        num_m = num_more_diag
        
        mas[i][0] = num_less_diag
        num_less_diag += 1
        new_num = num_less_diag
        
        mas[i][i] = num_m
        
# если m >= n, то выводится массив с элементами m-1 и так далее относительно главной диагонали
elif num_m >= num_n:
    for i in range(len(mas)):
        for j in range(len(mas)):
            if j > i:
                num_m -= 1
                mas[i][j] = num_m
            if j < i:
                mas[i][j] = new_num
                new_num += 1 
        num_m = num_more_diag
        
        mas[i][0] = num_less_diag
        num_less_diag -= 1
        new_num = num_less_diag
        
        mas[i][i] = num_m

# вывод массива
print("Требуемый массив:")
print(mas)
