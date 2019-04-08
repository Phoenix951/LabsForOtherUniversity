# Основы Python
# Задание 4

# переменные
decisions = []
z = 0
i = 0
res = 0

# введение переменных
a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))
d = int(input("Введите коэффициент d: "))
print(a, "x +", b, "y +", c, "z =", d)

# решение уравнения
value_des = int(input("Сколько решение вы хотите вывести: "))
while i != value_des:
    print("Введите произвольные числа: ")
    x = int(input("Введите произвольное число x: "))
    y = int(input("Введите произвольное число y: "))
    z = int((d - (a*x+b*y))/c)
    res = a*x + b*y + c*z
    if res == d:
        decisions.append([x, y, z])
    else:
        print("Это не решение")
    i += 1

# вывод решения
print("Список решений уравнения: ")
for i in range(len(decisions)):
    print((i + 1), "-й набор: ", decisions[i])

input("Enter")
