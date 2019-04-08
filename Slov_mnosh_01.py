# Программа по созданию покупателя

# Первоначальные данные
count = 0
BUYER = []
BUYERS_NAME = []
PRODUCTS_LIST = []
SORT_LIST = []
CUSTOMER = {}
key = 0

# введение количество покупателей
count = int(input("Введите количество покупателей: "))

# создаем список покупателей состоящий из словарей
while key < count:
    CUSTOMER['name'] = input("Введите имя и фамилию покупателя: ")
    CUSTOMER['product'] = input("Введите название товара: ")
    CUSTOMER['number'] = int(input("Введите количество купленных товаров: "))
    BUYER.append(CUSTOMER)
    CUSTOMER = {}
    key += 1

# создаем список всех купленных товаров каждым покупателем
for i in BUYER:
    new_name = i['name']
    if str(new_name) not in BUYERS_NAME:
        BUYERS_NAME.append(i['name'])
        for j in BUYER:
            if new_name == j['name']:
                new_sort = j['product'] + " Количество: " + str(j['number'])
                SORT_LIST.append(new_sort)
        # сортируем список по количеству товаров
        SORT_LIST.sort()
        PRODUCTS_LIST.append(str(new_name) + " " + str(SORT_LIST))
        SORT_LIST = []
    else:
        continue

# выводим список имен покупателей
print("Список имен покупателей:")
for i in BUYERS_NAME:
    print("Покупатель: ", i)

# выводим список товаров отсортированных по имени
PRODUCTS_LIST.sort()
for i in PRODUCTS_LIST:
    print(i)
