class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. [{task['status']}] {task['name']}")

    def add_task(self, name):
        self.tasks.append({'name': name, 'status': 'Incomplete'})

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['status'] = 'Completed'
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print(f"Task {task_number} removed.")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application:")
        print("1. Display To-Do List")
        print("2. Add a Task")
        print("3. Mark a Task as Completed")
        print("4. Remove a Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task_name = input("Enter the task's name: ")
            todo_list.add_task(task_name)
            print("Task added successfully.")
        elif choice == '3':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.complete_task(task_number)
        elif choice == '4':
            todo_list.display_tasks()
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
