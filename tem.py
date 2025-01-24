class Task:
    def _init_(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True
        print(f"Task '{self.title}' marked as completed.")

    def _str_(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}\nDescription: {self.description}"


class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed.")
                break  # Exit the loop after removing the task
        else:  # Execute if the loop completes without finding the task
            print(f"Task '{title}' not found.")
