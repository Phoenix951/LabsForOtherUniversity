# Основы Python
# Задание 1

# переменные
value_of_num = 0
newnumber_mas_deg_2 = []
numbers = []
deg = 2

value_N = float(input("Введите неотрицательное число N: "))
value_n = int(input("Введите величину степени n: "))

# создаем последовательность
numbers.append(2)
for i in range(3, int(value_N), 2):
    for j in numbers:
        if i%j == 0:
            break
    else:
        numbers.append(i)
        
# подсчет количества простых чисел
for i in numbers:
    value_of_num += 1
print("Количество простых чисел: ", value_of_num)

# копируем последовательность
numbers_deg = numbers[:]

# выводим первоначальную последовательность
print(" Простые числа: ", end=" ")
for i in numbers:  
    print(i, end=" ")

# создаем и выводи последовательности в зависимости от степени
while deg <= value_n:
    if deg == 2:
        print("\n Квадраты: ", end=" ")
    elif deg == 3:
        print("\n Кубы: ", end=" ")
    else:
        print("\n", deg, "-е степени: ", end=" ")
    for i in range(len(numbers)):
        numbers_deg[i] = numbers[i] ** deg
    for i in numbers_deg:  
        print(i, end=" ")
    deg += 1
    
input("\n\nНажмите Enter для выхода")
