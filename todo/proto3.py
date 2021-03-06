import json

class Todo:
    def __init__(self):
        self.todolist = []
        self.daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        self.filename = "save_folder/proto3.json"
    
    def helpUser(self):
        print('\nThis is todo list app!')
        print('Users can add tasks')
        print('Choose your appropriate day!')
        for days in self.daysOfWeek:
            if days:
                print(days)
                if days == self.daysOfWeek[-1]:
                    print(days)
                    print()
    
    def commit_tasks(self, addTasks):
        """pushes all the tasks in a json file for later use"""
        with open(self.filename, "w") as f:
            json.dump(addTasks, f)
    
    def read_tasks(self):
        """reads the json file"""
        with open(self.filename, "r") as f:
            data = json.load(f)
        print(data)

    # def removeTasks(self, theKey, rmTask):
    #     for tasks in self.todolist:
    #         for k,v in tasks.items():
    #             if theKey == k:
    #                 if rmTask in v:
    #                     v.remove(rmTask)

    def showTasks(self):
        if self.todolist:
            print()
            for tasks in self.todolist:
                for k, v in tasks.items():
                    print(f"{k.upper()}: ")
                    for number, tasks in enumerate(v):
                        print(f"\t{number + 1}. {tasks}\n")
            print()
        else:
            print("\nTodo list is empty!\n")


def buildTasks():
    key =  input("Enter a day of the weeK: ").title()
    temp_dict = {}
    tasks = []
    while True:
        task = input("Enter the task: ")
        if task:
            tasks.append(task)
        elif task == '':
            break
    temp_dict[key] = tasks
    return temp_dict

# create todo list object
myTasks = Todo()

# main loop
run = True   
while run:
    myTasks.helpUser()
    print('Choose to add tasks, remove tasks, or delete the entire todo list for the day.\n')

    choice = input("add, remove or delete or show or exit: ")
    if choice.lower() == 'add':
        todolists = buildTasks()
        myTasks.commit_tasks(todolists)
    # elif choice.lower() == 'remove':
    #     myTasks.showTasks()
    #     which_key = input("Which day of the week? ").title()
    #     removing_task = input("which task would you like removed: ")
    #     myTasks.removeTasks(which_key, removing_task)
    # elif choice.lower() == 'delete':
    #     myTasks.todolist = []
    elif choice.lower() == 'show':
        print(myTasks.todolist)
    else:
        run = False