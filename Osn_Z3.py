# Основы Python
# Задание 3

# переменные
numbers = []
newnumbers = []
step = 0
i = 0
new = ""
newi = 1
newi1 = 1
footstep = 0
footstep_new = 0
monot_up = 1
monot_down = 1

# выполнение
value = int(input("Количество цифр в последовательности: "))
while step < value:
    number = int(input("Введите число: "))
    numbers.append(number)
    step += 1

# проверка чисел меньших и больших предыдущего
newvalue = int(input("Введите позицию требуемого числа, идущего после проверяемого: "))
newvalue -= 2
for i in range(0, newvalue):
    if numbers[i] < numbers[newvalue]:
        footstep += 1
    elif numbers[i] > numbers[newvalue]:
        footstep_new += 1
print("Проверяемое число: ", numbers[newvalue])
print("Вот столько меньше проверямого числа: ", footstep)
print("Вот столько больше проверямого числа: ", footstep_new)

# проверка монотонности
for i in range(len(numbers)):
    if numbers[i] > numbers[i - 1]:
        monot_up += 1
    elif numbers[i] < numbers[i - 1]:
        monot_down += 1
if monot_up == len(numbers):
    print("Монотонность возрастающая.\n")
elif monot_down == len(numbers):
    print("Монотонность убывающая.\n")
else:
    print("Монотонность отсутствует.\n")

# сортировка
newnumber = 0
while newi1 < len(numbers):
    for i in range(len(numbers) - newi1):
        if numbers[i] > numbers[i+1]:
            newnumber = numbers[i + 1]
            numbers[i + 1] = numbers[i]
            numbers[i] = newnumber
    newi1 += 1
while i < len(numbers):
    newnumbers.append(str(numbers[i]))
    i += 1

# выведение списка в виде "лесенки"
print("Вот последовательность: ", numbers)
input("Нажмите Enter, чтобы получить лесенку.\n")
print("Требуемая лесенка: ")
for i in newnumbers:
    new += i
    print(new)

input("\nНажмите Enter чтобы выйти")
