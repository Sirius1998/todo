print("This is a todo list program.")
tasks = []
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
create = True
while create:
    activities = []
    ask = input("Enter add tasks or stop: (y/n) ")
    if ask.lower() == 'y':
        day = input("Enter todya's day of the week: ").title()
        if day in days:
            current_day = {}

            addingTasks = True
            while addingTasks:
                new_tasks = input("Enter new tasks: ")
                if new_tasks:
                      activities.append(new_tasks)
                else:
                    addingTasks = False
            current_day[day] = activities
            tasks.append(current_day)
    else:
            create = False

for task in tasks:
    for k, v in task.items():
        print(f"{k}:{v}")