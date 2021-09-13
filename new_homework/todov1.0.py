#Привет.
#Это ToDo list.
#v 1.0

#todolist = {task_number:task_info[]}

def mark_add(int):
    change_task = todolist[int]
    change_task.append(mark)
    todolist[int] = change_task
    return change_task

def mark_del(int):
    temp = todolist[int]
    del temp[1]
    todolist[int] = temp
    return temp
    
def task_add(int, text):
    todolist[int] = text
    return todolist

def todo_exit():
    ys = input('Данные не будут сохранены. Вы уверены?: ')
    ys.lower()
    if ys in ('д', 'да'):
        print('Хорошего дня!')
    exit()

def print_task():
    print(todolist, '\n')

    
todolist = {}
task_info = []
task_number = int()
mark = '- DONE'
choice = None
while choice != 0:
    print("""   
        Добро пожловать! Что будем делать?: 
    \t0. Завершить работу.
    \t1. Добавить задачу.
    \t2. Посмотреть список задач.
    \t3. Удалить задачу.
    \t4. Изменить задачу.
    \t5. Отметить задачу.
    \t6. Снять отметку с задачи.
    \t7. Отметить все задачт.
    \t8. Снять отметку со всех задач.
    \t9. Удалить отмеченные.
    """)
    
    
    choice = input('Ваш выбор?: ')

    if choice == '0':
        todo_exit()
    elif choice == '1':
        try:
            number = int(input('Введите номер задачи: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        task_info = [input('Описание задачи: ')]
        task_add(number, task_info)
    elif choice == '2':
        print('НОМЕР - ЗАДАЧА - ОТМЕТКА')
        #print(task_info)
        print_task()
    elif choice == '3':
        try:
            del_choice = int(input('Какой пункт удаляем?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        if del_choice in todolist:
            print(todolist.pop(del_choice),"удален!")
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
        mark_choice = int(input('Какой пункт отмечаем?: '))
        mark_add(mark_choice)
    elif choice == '6':
        del_mark = int(input('С какого пункта снимаем отметку?: '))
        mark_del(del_mark)
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