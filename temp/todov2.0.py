# todolist = {"task_info":[]}

import json
todolist = {}
mark = 'DONE!'

def add_list(number, task):
    todolist[number] = [task]
    return todolist

def print_add_list():
    number = input('Input task number: ')
    if number in todolist:
        print('There is already one, choose another.')
    task = input('Input task: ')
    add_list(number, task)
    print('Successfully!')
    print_task()

def print_task():
    print('Yours Task: ')
    print(todolist)

def delet_task():
    del_nub = input('Input number task for delete: ')
    todolist.pop(del_nub)
    print('Successfully!')
    print_task()
    return todolist

def mark_task():
    mark_num = input('Input task number for mark: ')
    mark_number = todolist[mark_num]
    mark_number.append(mark)
    todolist[mark_num] = mark_number
    print('Successfully!')
    print_task()
    return todolist

def del_mark_task():
    mark_num = input('Input task number for delete mark: ')
    del todolist[mark_num][1]
    print('Successfully!')
    print_task()
    return todolist
    
def all_mark():
    for value in todolist:
        temp_value = todolist[value]
        if mark not in temp_value:
            temp_value.append(mark)
            todolist[value] = temp_value
            print('Successfully!')
    print_task()
    return todolist

def del_all_mark():
    for all_mark in todolist:
        temp_value = todolist[all_mark]
        if mark in temp_value:
            del temp_value[1]
            todolist[all_mark] = temp_value
            print('Successfully!')
            print_task()
    return todolist

def check_mark_done():
    t = []
    for i in todolist:
        temp_task = todolist[i]
        if mark in temp_task:
            t += temp_task
    print('Successfully!')    
    print(t)
    
def check_mark_none_done():
    t = []
    for i in todolist:
        temp_task = todolist[i]
        if mark not in temp_task:
            t += temp_task
    print('Successfully!')    
    print(t)  
        
def find_task():
    find = input('Enter what we are looking for?   ')
    temp_task = []
    for i in todolist:
        temp_task = todolist[i][0]
        if find in temp_task:
            print(temp_task)

def save_and_exit():
    name_list = input('Enter your file names:  ')
    with open(name_list+'.json', 'w') as savefile:
        json.dump(todolist, savefile)
        print('Successfully! Good day!') 
        exit()

def only_exit():
    print('Good Day!')
    exit()

def  load_file():
    name = input('Enter file names: ')
    with open(name+'.json', 'r+') as loadfile:
        data=json.load(loadfile)
        print('Successfully!')
        return data

def load_todolist():
    global todolist
    todolist = load_file()

choices = {
     "1": print_add_list,
     "2": print_task,
     "3": delet_task,
     "4": mark_task,
     "5": del_mark_task,
     "6": all_mark,
     "7": del_all_mark,
     "8": check_mark_done,
     "9": check_mark_none_done,
     "10": find_task,
     "11": save_and_exit,
     "12": load_todolist,
     "13": only_exit
     }

menu = """
1. Add Task.
2. Show Tasks.
3. Delete Task.
4. Add mark task.
5. Delete mark task.
6. Mark all tasks.
7. Delete all marks.
8. Show executed only.
9. Show unexecuted.
10. Find tasks.
11. Save and Exit.
12. Load list.
13. Exit.

"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('Non valid menu option')
        continue
    choice()

