# программа для работы с файлами (альтернативный вариант)

# константы
OPERATION = ["r", "w", "x"]

# требуемые переменные
count_file = 0
count_oper = 0
new_key = 0
files = {}
files_oper = []

# выводится информация об возможных операциях
print("\nВозможные операции над файлами: ")
print("Открыть файл для чтения 1 -->", OPERATION[0])
print("Открыть файл для записи 2 -->", OPERATION[1])
print("Создать новый файл и открыть его для записи 3 -->", OPERATION[2])

files_number_N = int(input("\nВведите количество файлов: "))

while count_file < files_number_N:
    print("\nВозможные операции над файлами: ")
    print("Открыть файл для чтения 1 -->", OPERATION[0])
    print("Открыть файл для записи 2 -->", OPERATION[1])
    print("Создать новый файл и открыть его для записи 3 -->", OPERATION[2])
    file_name = input("\nВведите название файла: ")
    num_oper = int(input("\nВведите количество допустимых операций: "))
    while new_key < num_oper:
        choice_oper = int(input("\nВведите номер возможной операции: "))
        while choice_oper > 3:
            print("\n\tВыход за пределы количества допустимых операций.")
            choice_oper = int(input("Введите номер возможной операции: "))
        while OPERATION[choice_oper - 1] in files_oper:
            print("\n\tДанная комманда присутствует.")
            choice_oper = int(input("Введите номер возможной операции: "))
        files_oper.append(OPERATION[choice_oper - 1])
        new_key += 1
    new_key = 0
    files[file_name] = files_oper
    files_oper = []
    count_file += 1

# вывод всех файлов
print("\nФайлы: ")
print(files)

# задается количество требуемых запросов
num_of_req_M = int(input("Введите количество запросов: "))

# производится проверка наличия разрешенной операции к файлу
while count_oper < num_of_req_M:
    requir_oper = input("Введите название проверяемой операции: ")
    requir_file = input("Введите название проверяемого файла: ")
    if requir_oper in files[requir_file]:
        print("OK")
    else:
        print("Access denied")
    count_oper += 1
        
