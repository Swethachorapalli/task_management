from datetime import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, task_name, task_date):
        task = Task(task_name, task_date)
        self.tasks.append(task)
        print(f"Task '{task_name}' added for {self.username}.")

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed for {self.username}.")
                return
        else:
            print(f"Task '{task_name}' not found for {self.username}.")

    def show_tasks(self):
        print(f"To-do List for {self.username}:")
        for task in self.tasks:
            print(f"Task: {task.name} | Date: {task.date}")

class Task:
    def __init__(self, name, date):
        self.name = name
        self.date = date

users = {}

while True:
    print("\n****To-do List****")
    print("1. Create User")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Show Tasks")
    print("5. Exit")
    choice = input("Enter your Choice: ")

    if choice == "1":
        username = input("Enter username: ")
        if username not in users:
            users[username] = User(username)
            print(f"User '{username}' created Successfully.")
        else:
            print("Username already exists.")

    elif choice == "2":
        username = input("Enter username: ")
        if username in users:
            task_name = input("Enter task name: ")
            task_date = input("Enter task date (YYYY-MM-DD): ")
            try:
                datetime.strptime(task_date, "%Y-%m-%d")
                users[username].add_task(task_name, task_date)
            except ValueError:
                print("Invalid date format. Task not added.")
        else:
            print("User not found.")

    elif choice == "3":
        username = input("Enter username: ")
        if username in users:
            task_name = input("Enter task name: ")
            users[username].remove_task(task_name)
        else:
            print("User not found.")

    elif choice == "4":
        username = input("Enter username: ")
        if username in users:
            users[username].show_tasks()
        else:
            print("User not found.")

    elif choice == "5":
        break
    else:
        print("Invalid Choice. Please try again.")

print("Thank You For using the To-do List!!")