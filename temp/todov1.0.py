#Привет.
#Это ToDo list.
#v 1.0

#todolist = {task_number:task_info[]}

todolist = {}
task_info = []
task_number = int()
mark = '- DONE'
choice = None
while choice != 0:
    print("""   
    \tСписок задач. v 1.0.
        Добро пожловать! Что будем делать?: 
    \t0. Завершить раоту.
    \t1. Добавить задачу.
    \t2. Посмотреть список задач.
    \t3. Удалить задачу.
    \t4. Изменить задачу.
    \t5. Отметить задачу.
    \t6. Снять отметку с задачи.
    \t7. Отметить все задачт.
    \t8. Снять отметку со всех задач.
    """)
    
    #\t9. Удалить все задачи.
    
    
    choice = input('Ваш выбор?: ')

    if choice == '0':
        print('Всего хорошего!')
        break
    elif choice == '1':
        try:
            number = int(input('Введите номер задачи: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        task_info = [input('Описание задачи: ')]
        todolist[number] = task_info
    elif choice == '2':
        print('Список задач!')
        print('НОМЕР - ЗАДАЧА - ОТМЕТКА')
        print(todolist)
    elif choice == '3':
        try:
            del_choice = int(input('Какой пункт удаляем?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        if del_choice in todolist:
            del todolist[del_choice]
        else:
            print('Такого пункта нет.')
            continue
    elif choice == '4':
        try:
            edit_choice = int(input('Какой пункт изменяем?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        new_task = [input('Какая новая задача?: ')]
        todolist[edit_choice] = new_task
    elif choice == '5':
        try:
            mark_choice = int(input('Какой пункт отмечаем?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        change_task = todolist[mark_choice]
        change_task.append(mark)
        todolist[mark_choice] = change_task
    elif choice == '6':
        try:
            del_mark = int(input('С какого пункта снимаем отметку?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        temp = todolist[del_mark]
        del temp[1]
        todolist[del_mark] = temp
    elif choice == '7':
        for value in todolist:
            temp_value = todolist[value]
            temp_value.append(mark)
            todolist[value] = temp_value
        print('Все пункты отмечены.')
    elif choice == '8':
        for all_mark in todolist:
            temp_value = todolist[all_mark]
            del temp_value[1]
            todolist[all_mark] = temp_value
        print('Все отметки сняты.')
    else:
        print('В меню нет варианта', choice)
        continue