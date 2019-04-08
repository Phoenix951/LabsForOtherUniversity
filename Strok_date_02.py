# работа с текстом
import re
from datetime import datetime

# константы
DATE_FORM = ['%d-%m-%Y %H:%M']
SPEC_SYMB = """;:–_,.!@#$%^&*()~`"'[]{}\|/?\n0123456789"""
TEXT = """Строки в Python – упорядоченные последовательности символов , используемые для хранения и представления текстовой информации ,
поэтому с помощью loved строк 01-01-2014 21:24 можно работать со всем , что может быть представлено в текстовой форме .
Главное достоинство строк в loved тройных 01-09-2014 21:25 кавычках в том , что их можно rolled использовать для записи многострочных блоков текста .
Внутри такой строки loved возможно присутствие кавычек killed и апострофов 06-07-2014 21:12 , главное , чтобы не было трех кавычек подряд ."""


# переменные
word_mas = []
res_date = []
choice_sent = None
choice_letter = None
quantity_sent = 0
quantity_word = 0
quant_input = 0
let_key = 0
konkat = 0
eng_reg_verbs = 0

print("Вот исходный текст: \n", TEXT)
sentenses = TEXT.split(".")

for sent in sentenses:
    newsent = sent.replace("\n", "")
    if sent == "":
        continue
    words = newsent.split(" ")
    word_mas += words
    quantity_sent += 1

# работа с датами в тексте
date = re.findall(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}', TEXT)
date_day = str(re.findall(r'\d{2}-\d{2}-\d{4}', TEXT))
date_time = str(re.findall(r'\d{2}:\d{2}', TEXT))
print("Все даты (с временем) находящийся в тексте: \n", date)

# форматирование дат
for time in date:
    for formats in DATE_FORM:
        res_date.append(datetime.strptime(time, formats))

# Задание того, что требуется во время выведенных дат
for each_date in res_date:
    newdate = datetime.date(each_date)
    newtime = datetime.time(each_date)
    # Осенне-зимний семестр
    if newdate.month >= 9 and newdate.month <= 12:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Осенне-зимний семестр. Пора в баню.")
        # первая смена
        if newtime.hour > 14 and newtime.hour < 20:
            print("\tСейчас ", newtime.hour ," час (часов). Это было во вторую смену.")
        # вторая смена
        elif newtime.hour >= 8 and newtime.hour <= 14:
            print("\tСейчас ", newtime.hour ," час (часов). Это было в первую смену.")
        # время сна
        elif newtime.hour >= 0 and newtime.hour < 8 or newtime.hour >= 20 and newtime.hour <= 24:
            print("\tСейчас ", newtime.hour ," час (часов). В это время у меня сон.")
    # Зимне-весенний
    elif newdate.month > 2 and newdate.month < 6 or newdate.month == 2 and newdate.day > 5 or newdate.month == 6 and newdate.day <= 20:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Зимне-весенний семестр. Худеем к пляжу.")
        # первая смена
        if newtime.hour > 14 and newtime.hour < 20:
            print("\tСейчас ", newtime.hour ," час (часов). Это было во вторую смену.")
        # вторая смена
        elif newtime.hour >= 8 and newtime.hour <= 14:
            print("\tСейчас ", newtime.hour ," час (часов). Это было в первую смену.")
        # время сна
        elif newtime.hour >= 0 and newtime.hour < 8 or newtime.hour >= 20 and newtime.hour <= 24:
            print("\tСейчас ", newtime.hour ," час (часов). В это время у меня сон.")
    # Зимняя сессия
    elif newdate.month == 1 and newdate.day <= 20:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Зимняя сессия. Грустим, смотрим сериальчики и готовимся к экзаменам.")
    # Зимние каникулы
    elif newdate.month == 1 and newdate.day > 20 or newdate.month == 2 and newdate.day <= 5:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Зимние каникулы. Спим как медведи.")
    # Летняя сессия
    elif newdate.month == 6 and newdate.day > 20 or newdate.month == 7 and newdate.day <= 5:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Летняя сессия. Горим в прямом и переносном смысле.")
    # Летние каникулы
    elif newdate.month == 7 and newdate.day > 5 or newdate.month == 8:
        print("Сейчас ", newdate.month ," месяц и ", newdate.day ," день. Летние каникулы. ОТДЫЫЫЫЫЫЫЫЫХ")
                        
    
# проверка слов на наличие спец символов
for word in word_mas:
    if word in SPEC_SYMB or word == "" or word in date_day or word in date_time:
        continue 
    else:
        quantity_word += 1

print("\nКоличество предложений: ", quantity_sent)
print("Количество слов: ", quantity_word, "\n")

# выбор предложения
choice_sent = int(input("Введите номер требуемого предложения: "))
print("\nВыбранное предложение: ", sentenses[choice_sent])
sent_choice = sentenses[choice_sent]

# введение требуемой буквы для замены
choice_letter = input("\nВведите требуемую букву: ")

# часть предложения которая будет изменяться
new_sentense_up = sent_choice[2:len(sent_choice)-2].replace(choice_letter,choice_letter.upper())
new_sentense_down = sent_choice[2:len(sent_choice)-2].replace(choice_letter.upper(),choice_letter.lower())

# замена на верхний регистр
new_sentense = sent_choice[0:2]
new_sentense += new_sentense_up
new_sentense += sent_choice[len(sent_choice)-2:len(sent_choice)-1]

print("Выбранная строка после преобразования выбранной буквы в верхний регистр:\n", new_sentense, "\n")

# замена на нижний регистр
new_sentense = sent_choice[0:2]
new_sentense += new_sentense_down
new_sentense += sent_choice[len(sent_choice)-2:len(sent_choice)-1]

print("Выбранная строка после преобразования выбранной буквы в нижний регистр:\n", new_sentense, "\n")

# производится удаление из текста строки находящийся между m-ым и n-ым вхождением заданной буквы
require_let = input("Введите требуемую букву: ")
first_m = int(input("Введите m-ое вхождение буквы: "))
last_n = int(input("Введите n-ое вхождение буквы: "))

for letter in TEXT:
    konkat += 1
    if letter == require_let:
        let_key += 1
        if let_key == first_m: 
            new = TEXT.index(require_let, konkat-1)
        elif let_key == last_n:
            old = TEXT.index(require_let, konkat-1)

del_string = TEXT[new+1:old]
new_text = TEXT.replace(del_string, "")

print("Индекс m-ого вхождения введенной буквы: ", new)
print("Индекс n-ого вхождения введенной буквы: ", old, "\n")
print("Исходный текст:\n", TEXT, "\n")
print("Новый текст с удаленное строкой:\n", new_text, "\n")
print("Удаленная строка выведенная прямо:\n", del_string, "\n")
print("Удаленная строка выведенная обратно:\n", del_string[::-1], "\n")
print("Новый текст с удаленное строкой выведенный в обратном порядке:\n", new_text[::-1], "\n")
print("Новый текст с удаленное строкой выведенный в обратном порядке через одну букву:\n", new_text[::-2], "\n")

# поиск английских глаголов
for word in word_mas:
    if word in SPEC_SYMB or word == "":
        continue 
    elif word[len(word)-2:len(word)] == "ed":
        eng_reg_verbs += 1

print("В тексте присутствуют ", eng_reg_verbs, "правильных английских глагола во второй форме.\n")


input("Enter")
