# todolist = {"task_info":[]}

import json
todolist = {}
mark = 'DONE!'
norm_numb = '1,2,3,4,5,6,7,8,9,0'
save_list = []

def yes_no_dec(func):
    def wrapper(*args,**kvargs):
        while True:
            result  = func(*args,**kvargs)
            print('Successfully!')
            print_task()
            if not yes_no_todo_choice():
                break
        return result
    return wrapper

def succ_dec(func):
    def wrapper(*args, **kvargs):
        result = func (*args, **kvargs)
        print('Successfully!')
        print_task()
        return result
    return wrapper

def add_list(number, task):
    todolist[number] = [task]
    return todolist

@yes_no_dec
def print_add_list():
    while True:
        number = input('Input task number: ')
        if number not in norm_numb:
            print('Only numbers')
            break
        task = input('Input task: ')
        return add_list(number, task)

def print_task():
    print('Yours Task:')
    for i in todolist:
        val = todolist[i]
        print(i, '-', val)

@yes_no_dec
def delet_task():
    while True:
        del_nub = input('Input number task for delete: ')
        if del_nub not in todolist:
            print('There is no task with this number. ')
            break
        todolist.pop(del_nub)
        return todolist

@yes_no_dec
def mark_task():
    while True:
        mark_num = input('Input task number for mark: ')
        if mark_num not in todolist:
            print('There is no task with this number. ')
            break
        mark_number = todolist[mark_num]
        mark_number.append(mark)
        todolist[mark_num] = mark_number
        return todolist

@yes_no_dec
def del_mark_task():
    while True:
        mark_num = input('Input task number for delete mark: ')
        if mark_num not in todolist:
            print('There is no task with this number. ')
            break
        del todolist[mark_num][1]
        return todolist

@succ_dec   
def all_mark():
    for value in todolist:
        temp_value = todolist[value]
        if mark not in temp_value:
            temp_value.append(mark)
            todolist[value] = temp_value
    return todolist

@succ_dec
def del_all_mark():
    for all_mark in todolist:
        temp_value = todolist[all_mark]
        if mark in temp_value:
            del temp_value[1]
            todolist[all_mark] = temp_value
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
    save_list.append(name_list)
    with open('save_list.json', 'w') as savelist:
        json.dump(save_list, savelist)
    with open(name_list+'.json', 'w') as savefile:
        json.dump(todolist, savefile)
        print('Successfully! Good day!') 
        exit()

def show_save_list():
    print('Your Save file:')
    with open('save_list.json', 'r+') as loadlist:
        data_s=json.load(loadlist)
        save_list.append(data_s)
    print(save_list)

def only_exit():
    print('Good Day!')
    exit()

def load_file():
    with open('save_list.json', 'r+') as loadlist:
        data_s=json.load(loadlist)
        save_list.append(data_s)
    print('Saved files: ', save_list)
    name = input('Enter file names: ')
    with open(name+'.json', 'r+') as loadfile:
        data=json.load(loadfile)
        print('Successfully!')
        return data

def load_todolist():
    global todolist
    todolist = load_file()

def yes_no_todo_choice():
     y = input(f'Do you want to another one? (y/n) ')
     return y in ('y', 'Y')

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
     "13": only_exit,
     "14": show_save_list
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
14. Show Save list.

"""

while True:
    menu_number = input(menu)
    choice = choices.get(menu_number)
    if not choice:
        print('Non valid menu option')
        continue
    choice()

