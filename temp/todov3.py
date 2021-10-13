import json

class Task:
    counter = 1
    def __init__(self,task='',is_done=False):
        self.task = task
        self.is_done = is_done
        self.number = Task.counter
        Task.counter += 1
    
    def __repr__(self) -> str:
        return f'№ {self.number}: {self.task} {"DONE" if self.is_done else "" }'
    
class Tasklist:
    task_list = []

    def add_task(self,text):
        self.task_list.append(Task(text))

    def print_tasks(self):
        for i in self.task_list:
            print(i)    

    def del_task(self,del_num):
        for num, el in enumerate(self.task_list):
            if el.number == del_num:
                self.task_list.pop(num)

    def done_task(self, mark_num):
        for num, el in enumerate(self.task_list):
            if el.number == mark_num:
                el.is_done = True

    def unmark_task(self, unmark_num):
        for num, el in enumerate(self.task_list):
            if el.number == unmark_num:
                el.is_done = False
    
    def all_done_task(self):
        for num, el in enumerate(self.task_list):
            el.is_done = True

    def unmark_all_task(self):
        for num, el in enumerate(self.task_list):
            el.is_done = False

    def only_done(self):
        t = []
        for num, el in enumerate(self.task_list):
            if el.is_done == True:
                t.append(el)
        print('Successfully!')    
        print(t)

    def only_undone(self):
        t = []
        for num, el in enumerate(self.task_list):
            if el.is_done == False:
                t.append(el)
        print('Successfully!')    
        print(t)

    def fnd_task(self, find):
        temp_task = []
        for num, el in enumerate(self.task_list):
            if el.task in find:
                temp_task.append(el)
                print(temp_task)

    def s_a_e(self,name):
        temp_task = []
        for num, el in enumerate(self.task_list):
            temp_task.append(el.task)
        with open(name+'.json', 'w') as savefile:
            json.dump(temp_task, savefile)

    def ld_file(self,name):
        with open(name+'.json', 'r+') as loadfile:
            data=json.load(loadfile)
            for i in data:
                self.task_list.append(Task(i))             

# class Save(Tasklist):
#     def s_a_e(self,name, format):
#         temp_task = []
#         for num, el in enumerate(self.task_list):
#             temp_task.append(el.task)
#         with open(name+'.'+format, 'w') as savefile:
#             format.dump(temp_task, savefile)
#             temp_task.clear()

#     def ld_file(self,name, format):
#         with open(name+'.'+format, 'r+') as loadfile:
#             data=format.load(loadfile)
#             for i in data:
#                 self.task_list.append(Task(i)) 


# class Savejson(Save):
#     def s_a_e(self, name, format='json'):
#         return super().s_a_e(name, format)

def yes_no_dec(func):
    def wrapper(*args,**kvargs):
        while True:
            result  = func(*args,**kvargs)
            print('Successfully!')
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

@yes_no_dec
def print_add_list():
    tusk = Tasklist()
    tusk.add_task(input('Input task: '))
    
    
def print_task():
    print('Yours Task:')
    a = Tasklist()
    a.print_tasks()
    

@yes_no_dec
def delet_task():
    del_nub = int(input('Input number task for delete: '))
    a = Tasklist()
    a.del_task(del_nub)
    

@yes_no_dec
def mark_task():
    mark_num = int(input('Input task number for mark: '))
    a=Tasklist()
    a.done_task(mark_num)

@yes_no_dec
def del_mark_task():
    unmark_num = int(input('Input task number for delete mark: '))
    a=Tasklist()
    a.unmark_task(unmark_num)

@succ_dec   
def all_mark():
    a = Tasklist()
    a.all_done_task()

@succ_dec
def del_all_mark():
    a = Tasklist()
    a.unmark_all_task()

def check_mark_done():
    a = Tasklist()
    a.only_done()
    
def check_mark_none_done():
    a = Tasklist()
    a.only_undone()
        
def find_task():
    find = input('Enter what we are looking for?   ')
    a = Tasklist()
    a.fnd_task(find)

def save_and_exit():
    name_list = input('Enter your file names:  ')
    a = Savejson()
    a.s_a_e(name_list)
    print('Successfully! Good day!') 
    exit()

def only_exit():
    print('Good Day!')
    exit()

def load_todolist():
    name = input('Enter file names: ')
    a = Tasklist()
    a.ld_file(name)

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
     "13": only_exit
     }

menu = """
____________________________
| 1.  | Add Task.           |
| 2.  | Show Tasks.         |
| 3.  | Delete Task.        |
| 4.  | Add mark task.      |
| 5.  | Delete mark task.   |
| 6.  | Mark all tasks.     |
| 7.  | Delete all marks.   |
| 8.  | Show executed only. |
| 9.  | Show unexecuted.    |
| 10. | Find tasks.         |
| 11. | Save and Exit.      |
| 12. | Load list.          |
| 13. | Exit.               |
|_____|_____________________|

Input menu number:  
"""

while True:
    menu_number = input(menu) 
    choice = choices.get(menu_number)
    if not choice:
        print('Non valid menu option')
        continue
    choice()