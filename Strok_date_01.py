# В заданных массивах строк программа проверяет наличие требуемых букв, а также производит требуемую замену

# константы
LETTERS = "аеоиaeoi"
VOWELS = "аеiouaеёиоуыэюя"
CONSONANTS = "bcdfghjklmnpqrstvwxzбвгджзклмнпрстфхцчшщ"
GOV_NUMBER = "abeikmhopctxавекмнорстх"
RUS_LETTER = "ёиуыэюябгджзлпфцчшщ"
ENG_LETTER = "udfgjlnqrsvwxz"
NAME_RUS = "Иван Иванович Иванов"
NAME_ENG = "Ivan Ivanovich Ivanov"

# Переменные
quanty_a_rus = 0
quanty_e_rus = 0
quanty_i_rus = 0
quanty_o_rus = 0
quanty_a = 0
quanty_e = 0
quanty_i = 0
quanty_o = 0
key_rus = 0
key_eng = 0
new_key = 0
name_rus_mas = []
name_eng_mas = []
new_string_rus = ""
new_string_eng = ""
string_number_rus = ""
string_number_eng = ""
sections_string = ""
new_sections_string = ""

# перевод строк в массивы
for letter in NAME_RUS:
    if letter.lower():
        if letter == " ":
            continue
        name_rus_mas += letter

for letter in NAME_ENG:
    if letter.lower():
        if letter == " ":
            continue
        name_eng_mas += letter

# выведение массивов    
print("Заданный массив на русском: \n", name_rus_mas)
print("Заданный массив на английском: \n", name_eng_mas)

print("\n\tРабота с русским массивом:")
# проверка массивов на наличие заданных букв в русском массиве
position = 0
for new_letter in name_rus_mas:
    position += 1
    if new_letter.lower() == "а":
        quanty_a_rus += 1
    elif new_letter.lower() == "и":
        quanty_i_rus += 1
    elif new_letter.lower() == "е":
        quanty_e_rus += 1
    elif new_letter.lower() == "о":
        quanty_o_rus += 1
    if new_letter.lower() in LETTERS:
        print("Позиция русской буквы: ", new_letter, " равна ", position)

# выведение числа вхождения заданных букв в русском массиве
print("Вхождение русской буквы 'а': ", quanty_a_rus)
print("Вхождение русской буквы 'и': ", quanty_i_rus)
print("Вхождение русской буквы 'е': ", quanty_e_rus)
print("Вхождение русской буквы 'о': ", quanty_o_rus)

print("\n\tРабота с английским массивом:")
# проверка массивов на наличие заданных букв в английском массиве
position = 0
for new_letter in name_eng_mas:
    position += 1
    if new_letter.lower() == "a":
        quanty_a += 1
    elif new_letter.lower() == "i":
        quanty_i += 1
    elif new_letter.lower() == "e":
        quanty_e += 1
    elif new_letter.lower() == "o":
        quanty_o += 1
    if new_letter.lower() in LETTERS:
        print("Позиция английской буквы: ", new_letter, " равна ", position)

# выведение числа вхождения заданных букв в английском массиве
print("Вхождение английской буквы 'а': ", quanty_a)
print("Вхождение английской буквы 'и': ", quanty_i)
print("Вхождение английской буквы 'е': ", quanty_e)
print("Вхождение английской буквы 'о': ", quanty_o)

# перевод русского массива в 0 и 1
for letter in NAME_RUS:
    if letter.lower():
        if letter == " ":
            continue
        if letter.lower() in VOWELS:
            letter = "1"
            new_string_rus += letter
        elif letter.lower() in CONSONANTS:
            letter = "0"
            new_string_rus += letter

print(new_string_rus)
for letter in new_string_rus:
    key_rus += 1
    string_number_rus += letter
    if string_number_rus == "101" and key_rus < 13:
        print(string_number_rus, ": 5")
        string_number_rus = ""
    elif string_number_rus == "010" and key_rus < 13:
        print(string_number_rus, ": 2")
        string_number_rus = ""
    elif string_number_rus == "101010":
        print(string_number_rus, ": 52")

# перевод английского массива в 0 и 1
for letter in NAME_ENG:
    if letter.lower():
        if letter == " ":
            continue
        if letter.lower() in VOWELS:
            letter = "1"
            new_string_eng += letter
        elif letter.lower() in CONSONANTS:
            letter = "0"
            new_string_eng += letter

print(new_string_eng)
for letter in new_string_eng:
    key_eng += 1
    string_number_eng += letter
    if string_number_eng == "101" and key_eng < 13:
        print(string_number_eng, ": 5")
        string_number_eng = ""
    elif string_number_eng == "010" and key_eng < 13:
        print(string_number_eng, ": 2")
        string_number_eng = ""
    elif string_number_eng == "0101010":
        print(string_number_eng, ": 52")

# объединение строк
general_string = NAME_RUS + " " + NAME_ENG
new_gen_string = ""
print("Строка после объединения двух первоначальных строк:\n", general_string)

for letter in general_string:
    if letter == " ":
        continue
    elif letter.lower() in RUS_LETTER:
        letter = "1"
        new_gen_string += letter
    elif letter.lower() in ENG_LETTER:
        letter = "2"
        new_gen_string += letter
    elif letter.lower() in GOV_NUMBER:
        letter = "3"
        new_gen_string += letter

print("Преобразованная строка:\n", new_gen_string)

# создание строки элементами которой являюся буквы отчества
for letter in general_string[5:13],general_string[26:35]:
    if letter.lower() in sections_string:
        continue
    sections_string += letter.lower()
    
print("Выборка по строке:\n", sections_string)

# создание строки элементами которой являюся буквы отчества
for newletter in sections_string:
    for letter in general_string[:4],general_string[14:25],general_string[36:]:
        if letter == " ":
            continue
        if letter.lower() == newletter.lower():
            new_key += 1
        if newletter.lower() in new_sections_string:
            continue
        if new_key <= 2:
            new_sections_string += newletter.lower()
        new_key = 0
        
print("Новая выборка по строке:\n", new_sections_string)
input("Enter")
