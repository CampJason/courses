#Привет.
#Это ToDo list.
#v 1.0

#todolist = {task_number:task_info[]}

todolist = {}
task_info = []
task_number = int()
mark = ' - DONE'
choice = None

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

def check_mark_done(todolist):
    t = []
    for i in todolist:
        temp_task = todolist[i]
        if mark in temp_task:
            t += temp_task
    return t
    
def check_mark_none_done(todolist):
    t = []
    for i in todolist:
        temp_task = todolist[i]
        if mark not in temp_task:
            t += temp_task
    return t    

def find_task(todolist, find):
    temp_task = []
    for i in todolist:
        temp_task = todolist[i][0]
        if find in temp_task:
            return temp_task


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
    \t9. Отфильтровать выполненные.
    \t10. Отфильтровать не выполненные.
    \t11. Поиск задачию.
    
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
        print_task()
    elif choice == '2':
        print('НОМЕР - ЗАДАЧА - ОТМЕТКА')
        
        print_task()
    elif choice == '3':
        try:
            del_choice = int(input('Какой пункт удаляем?: '))
        except ValueError:
            print('Неверное значение. Номер задачи может состоять только из целых чисел.')
            continue
        if del_choice in todolist:
            print(todolist.pop(del_choice),"удален!")
            print_task()
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
        print_task()
    elif choice == '5':
        mark_choice = int(input('Какой пункт отмечаем?: '))
        mark_add(mark_choice)
        print_task()
    elif choice == '6':
        del_mark = int(input('С какого пункта снимаем отметку?: '))
        mark_del(del_mark)
        print_task()
    elif choice == '7':
        for value in todolist:
            temp_value = todolist[value]
            if mark not in temp_value:
                temp_value.append(mark)
                todolist[value] = temp_value
        print('Все пункты отмечены.')
        print_task()
    elif choice == '8':
        for all_mark in todolist:
            temp_value = todolist[all_mark]
            if mark in temp_value:
                del temp_value[1]
                todolist[all_mark] = temp_value
        print('Все отметки сняты.')
        print_task()
    elif choice == '9':
        task_with_mark = check_mark_done(todolist)
        print(task_with_mark)
        print_task()
    elif choice == '10':
        task_none_mark = check_mark_none_done(todolist)
        print(task_none_mark)   
    elif choice == '11':
        find = input('Введите ключевое слово для поиска: ')
        print(find_task(todolist, find))
    else:
        print('В меню нет варианта', choice)
        continue