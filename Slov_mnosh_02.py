# программа для работы с файлами

# требуемые переменные
choice = None
files_number_N = None
files = {}
files_name = []
count_oper = 0
key = 0
num_of_oper_M = 0

# основное меню
while choice != '0':
    print("""\n\t\tМеню выбора действий:
    0 - Выйти
    1 - Записать название файла
    2 - Вывести список имеющихся файлов
    3 - Выбрать и прочитать файл
    4 - Выбрать и записать в файл
    5 - Создать новый файл (будет выполнено только в том случае, если файла не существует)
    6 - Вывести статиситику операций над всеми файлами
    """)
    # выбор пункта меню
    choice = input("Введите Ваш выбор: ")
    # пункт выхода
    if choice == '0':
        break
    # пункт для введения названия файла
    elif choice == '1':
        files_number_N = int(input("Введите количество файлов:\n"))
        while key < files_number_N:
            name = input("Введите название файла:\n")
            files_name.append(name + ".txt")
            key += 1
        # создаем словарь для занесения числа операций над всеми файлами
        for i in files_name:
            files[i] = num_of_oper_M
    # пункт для выведения списка всех имеющихся файлов
    elif choice == '2':
        print("\nФайлы: ")
        for i in files_name:
            print(i)
    # пункт для чтения выбранного файла
    elif choice == '3':
        num_file = int(input("Введите номер требуемого файла: "))
        # проверка существования файла в системе
        if num_file >= len(files_name):
            while num_file >= len(files_name):
                print("Файла под таким номер нет. Введите новый номер.")
                num_file = int(input("Введите номер требуемого файла: "))
        # увеличение числа произведенных операций
        for i in files:
            if files_name[num_file] == i:
                files[i] += 1
        # выведение содержимого файла
        print("Содержимое вашего файла: ")
        text_file = open(files_name[num_file], "r", encoding='utf-8')
        whole_file = text_file.read()
        print(whole_file)
        text_file.close()
    # пункт для перезаписи в выбранный файл
    elif choice == '4':
        num_file = int(input("Введите номер требуемого файла: "))
        # проверка существования файла в системе
        if num_file >= len(files_name):
            while num_file >= len(files_name):
                print("Файла под таким номер нет. Введите новый номер.")
                num_file = int(input("Введите номер требуемого файла: "))
        # увеличение числа произведенных операций
        for i in files:
            if files_name[num_file] == i:
                files[i] += 1
        text_file = open(files_name[num_file], "w", encoding='utf-8')
        your_string = input("Введите строку для добавления:\n")
        text_file.write(your_string)
        text_file.close()
    # пункт для создания нового файла
    elif choice == '5':
        name = input("Введите название файла:\n")
        files_name.append(name + ".txt")
        text_file = open(name + ".txt", "x", encoding='utf-8')
        your_string = input("Введите строку для добавления:\n")
        text_file.write(your_string)
        text_file.close()
    # пункт для вывода словаря операций
    elif choice == '6':
        print(files)
    else:
        print("\nТакого пункта нет.")
    

