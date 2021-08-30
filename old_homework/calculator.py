first_number = float(input('Введите первое число: '))
sign = input('Какое действие? ')
second_number = float(input('Введите второе число: '))
if sign == '+':
    print(first_number+second_number)
elif sign == '-':
    print(first_number-second_number)
elif sign == '/':
    print(first_number/second_number)
elif sign == '*':
    print(first_number*second_number)
else:
    print('Error')
