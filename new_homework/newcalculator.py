cont = '='
while cont == '=':
    try:
        first_number = float(input('Введите число: '))
    except ValueError:
        print('Это не цифра. Попробуйте заново.')
        continue
    operation = input('Операция (+, -, *, /, //, **, %, <, >, ==): ')
    try:
        second_number = float(input('Введите число: '))
    except ValueError:
        print('Это не цифра. Попробуйте заново.')
        continue
    if operation == '+':
        print(first_number+second_number)
    elif operation == '-':
        print(first_number-second_number)
    elif operation == '/':
        try: 
            print(first_number/second_number)
        except ZeroDivisionError:
            print(0)
    elif operation == '*':
        print(first_number*second_number)
    elif operation == '//':
        print(first_number//second_number)
    elif operation == '**':
        print(first_number**second_number)
    elif operation == '%':
        print(first_number%second_number)
    elif operation == '<':
        print(first_number<second_number)
    elif operation == '>':
        print(first_number>second_number)
    elif operation == '==':
        print(first_number==second_number)
    else:
        print('Выбрана некорректная операция. Попробуйте заново.')
        continue
    cont = input('Введите = для продолжения или 0 для завершения. ')
    if cont == '0':
        break