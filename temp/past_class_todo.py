class Task:
    counter = 1
    def __init__(self,task=''):
        self.task = task
        self.mark = ''
        self.number = Task.counter
        Task.counter += 1
    
    def task_info(self):
        return self.number, self.task, self.mark

    def change_mark(self):
        self.mark = "DONE"
        return self.mark

    def unchange_mark(self):
        self.mark = ""
        return self.mark

class Tasklist:
    def __init__(self):
        self._task_list = []

    def add_task(self,text):
        self._task_list.append(Task(text))

    def print_tasks(self):
        for i in self._task_list:
            print(Task.task_info(i))

    def del_task(self,num):
        del_task_list = []
        for i in self._task_list:
            del_task_list.append(Task.task_info(i))
            if num in del_task_list:
                self._task_list.pop(i)
    
    def mark_tasks(self,num):
        mark_task_list = []
        for i in self._task_list:
            mark_task_list.append(Task.task_info(i))
            if num in mark_task_list:
                Task.change_mark(i)

    def del_mark_task(self, num):
        delmarktask = []
        for i in self._task_list:
            delmarktask.append(Task.task_info(i))
            if num in delmarktask:
                Task.unchange_mark(i)

    def mark_all_task(self):
        allmarktask = []
        for i in self._task_list:
            allmarktask.append(Task.task_info(i))
            Task.change_mark(i)