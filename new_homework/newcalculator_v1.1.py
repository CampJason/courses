first_number = float(input('Введите число: '))

operation = input('Операция (+, -, *, /, //, **, %, <, >, ==): ')

while operation != '=':
    
    second_number = float(input('Введите число: '))
   
    if operation == '+':
        result = first_number+second_number
        print(result)
    elif operation == '-':
        result = first_number-second_number
        print(result)
    elif operation == '/':
        try: 
            result = first_number/second_number
        except ZeroDivisionError:
            result=0
            print(result)
    elif operation == '*':
        result = first_number*second_number
        print(result)
    elif operation == '//':
        result = first_number//second_number
        print(result)
    elif operation == '**':
        result = first_number**second_number
        print(result)
    elif operation == '%':
        result = first_number%second_number
        print(result)
    elif operation == '<':
        result = first_number<second_number
        print(result)
    elif operation == '>':
        result = first_number>second_number
        print(result)
    elif operation == '==':
        result = first_number==second_number
        print(result)
    

    first_number = result
    operation = input('Операция (+, -, *, /, //, **, %, <, >, ==) или Q для завершения: ')
    if operation == "Q":
        break