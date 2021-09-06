#It's my homework about str methods.
#name: WTsm
#Russian language
#сделать получилось только апппер и ловер

# Сделаю функцию для увеличения:
def my_upper(text:str) -> str:
    text_letter = list(text)
    small_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    big_letters = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    step_1 = 0
    for letter in text_letter:
        if letter in small_letters:
            step_2 = 0
            for latter_letters in small_letters:
                if letter == latter_letters:
                    index_letter = step_2
                step_2 += 1
            text_letter[step_1] = big_letters[index_letter]
        step_1 = step_1 + 1
    return ''.join(text_letter)

# Сделаю функцию для уменшения
def my_lower(text:str) -> str:
    text_letter = list(text)
    small_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    big_letters = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    step_1 = 0
    for letter in text_letter:
        if letter in big_letters:
            step_2 = 0
            for latter_letters in big_letters:
                if letter == latter_letters:
                    index_letter = step_2
                step_2 += 1
            text_letter[step_1] = small_letters[index_letter]
        step_1 = step_1 + 1
    return ''.join(text_letter)


print('Привет. Постараюсь помочь с преобразованием текста.')
while True:
    text = input('С каким текстом будем работать?: ')
    if text == '':
        continue
    method = input("Что хотим сделать?:\n1 Увеличить регистр букв. \n2 Уменьшить регистр букв. \n3 Сделать первую букву заглавной. \n4 Все первые буквы фразы заглавные. \n5 Узнать, можно ли преобразовать строку в цифры. \n6 Заменить часть текста. \n7 Разделить на разные списки. \n8 Разделить чем-то. \n9 Выйти \n: ")
    if method == '1':
        print(my_upper(text))
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '2':
        print(my_lower(text))
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '3':
        print(text.capitalize())
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '4':
        print(text.title())
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '5':
        print(text.isdigit())
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д'or answer_user == 'д':
            continue
    elif method == '6':
        repl_a = input('Что меняем?: ')
        repl_b = input('На что меняем?: ')
        print(text.replace(repl_a, repl_b))
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н'or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '7':
        print(text.split())
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д'or answer_user == 'д':
            continue
    elif method == '8':
        repl_c = input('Чем будем разделять?: ' or answer_user == 'н')
        print(repl_c.join(text))
        answer_user = input('Продолжим? Д/Н: ' or answer_user == 'д')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '9':
        print('Хорошего дня.')
        break

