# todo_list.py

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_name):
        """Create a new task"""
        if task_name not in self.tasks:
            self.tasks[task_name] = False
            print(f"Task '{task_name}' created successfully!")
        else:
            print(f"Task '{task_name}' already exists!")

    def update_task(self, task_name, new_task_name):
        """Update an existing task"""
        if task_name in self.tasks:
            self.tasks[new_task_name] = self.tasks.pop(task_name)
            print(f"Task '{task_name}' updated to '{new_task_name}' successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def delete_task(self, task_name):
        """Delete a task"""
        if task_name in self.tasks:
            del self.tasks[task_name]
            print(f"Task '{task_name}' deleted successfully!")
        else:
            print(f"Task '{task_name}' not found!")

    def mark_task_completed(self, task_name):
        """Mark a task as completed"""
        if task_name in self.tasks:
            self.tasks[task_name] = True
            print(f"Task '{task_name}' marked as completed!")
        else:
            print(f"Task '{task_name}' not found!")

    def display_tasks(self):
        """Display all tasks"""
        print("To-Do List:")
        for task, status in self.tasks.items():
            status_str = "Completed" if status else "Pending"
            print(f"- {task}: {status_str}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Create task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Mark task completed")
        print("5. Display tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            todo_list.create_task(task_name)
        elif choice == "2":
            task_name = input("Enter task name: ")
            new_task_name = input("Enter new task name: ")
            todo_list.update_task(task_name, new_task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            todo_list.delete_task(task_name)
        elif choice == "4":
            task_name = input("Enter task name: ")
            todo_list.mark_task_completed(task_name)
        elif choice == "5":
            todo_list.display_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()