# Основы Python
# Задание 2

# переменные
numbers = []
newnumbers_max_mas = []
newnumbers_min_mas = []
i = 0
newnumber_max = None
newnumber_min = None
footstep_max = 0
footstep_min = 0

# цикл последовательности
choice = int(input("Введите величину последовательности (больше двух чисел): "))
while i != choice:
    if choice <= 2:
        choice = int(input("Последовательность должна быть больше 2. Введите величину последовательности: "))
    else:
        number = int(input("Введите число последовательности: "))
        numbers.append(number)
        i += 1
print("Введенная последовательность: ", numbers)

# минимальное и максимальное число
a = min(numbers)
b = max(numbers)

# циклы создания новых последовательностей, для выборки максимального и минимального числа
for i in range(len(numbers)):
    if numbers[i] < b:
        newnumber_max = numbers[i]
        newnumbers_max_mas.append(newnumber_max)
for i in range(len(numbers)):
    if numbers[i] > a:
        newnumber_min = numbers[i]
        newnumbers_min_mas.append(newnumber_min)

# минимальное и максимальное число из последовательностей проведенной выборки
amax = max(newnumbers_max_mas)
bmin = min(newnumbers_min_mas)

# циклы для подсчитывания количества минимального и максимального чисел
print("\n")
for i in range(len(numbers)):
    if numbers[i] == amax:
        print("Номер позиции максимального элемента: ", i + 1)
        footstep_max += 1
print("Число меньшее максимального: ", amax)
print("Число вхождений максимального числа: ", footstep_max, "\n") 
for i in range(len(numbers)):
    if numbers[i] == bmin:
        print("Номер позиции минимального элемента: ", i + 1)
        footstep_min += 1
print("Число большее минимального: ", bmin)
print("Число вхождений минимального числа: ", footstep_min)

input("\nНажмите Enter для выхода")
