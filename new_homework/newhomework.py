#It's my homework about str methods.
#name: WTsm
#Russian language

small_letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
big_letters = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

def my_upper(text:str):
    text_letter = list(text)
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

def my_lower(text:str):
    text_letter = list(text)
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

def my_isdigit(x):
    while x:
        try:
            get_number = int(x)
            answer = True
        except ValueError:
            if x == '0':
                answer = True
            elif x == '':
                print("Пожалуста, введите информацию: ")
                x = input()
                continue
            else:
                answer = False
                break
        else:
            break
    return answer

def my_titling(string):
    new_string = []
    if string[0] in small_letters:
        letter_index = small_letters.index(string[0])
        new_string.append(big_letters[letter_index])
        is_a_letter_before = True
    else:
        new_string.append(string[0])
        if new_string[0] in small_letters or new_string[0] in big_letters:
            is_a_letter_before = True
        else:
            is_a_letter_before = False
    string2 = string[1:]
    for i in range(len(string2)):
        if is_a_letter_before == True:
            new_string.append(string2[i])
            if string2[i] in small_letters or string2[i] in big_letters:
                is_a_letter_before = True
            else:
                is_a_letter_before = False
            i += 1
            continue
        elif is_a_letter_before == False:
            if string2[i] in small_letters:
                letter_index = small_letters.index(string2[i])
                new_string.append(big_letters[letter_index])
                is_a_letter_before = True
                i += 1
                continue
            else:
                new_string.append(string2[i])
                if string2[i] in small_letters or string2[i] in big_letters:
                    is_a_letter_before = True
                else:
                    is_a_letter_before = False
                i += 1
                continue
    return  new_string

print('Привет. Постараюсь помочь с преобразованием текста.')
while True:
    text = input('С каким текстом будем работать?: ')
    if text == '':
        continue
    method = input("""
    Что хотим сделать?:
    1. Увеличить регистр букв. 
    2. Уменьшить регистр букв. 
    3. Сделать первую букву заглавной.
    4. Все первые буквы фразы заглавные. 
    5. Узнать, можно ли преобразовать строку в цифры. 
    6. Заменить часть текста. 
    7. Разделить на разные списки. 
    8. Разделить чем-то. 
    9. Выйти: 
    """)
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
        titl = my_titling(text)
        print(''.join(titl))
        answer_user = input('Продолжим? Д/Н: ')
        if answer_user == 'Н' or answer_user == 'н':
            break
        elif answer_user == 'Д' or answer_user == 'д':
            continue
    elif method == '5':
        print(my_isdigit(text))
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

