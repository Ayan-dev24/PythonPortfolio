while True:
    print("\n1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Enter your decision: ")

    if choice == "1":
        task = input("Enter the task: ")
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task Saved. ✅")

    elif choice == "2":
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(lines):
                print(f"{index + 1}. {task.strip()}")

    elif choice == "3":
        with open("tasks.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No tasks to delete.")
        else:
            print("\nSelect a task to delete:")
            for index, task in enumerate(lines):
                print(f"{index + 1}. {task.strip()}")

            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(lines):
                    lines.pop(num - 1)

                    with open("tasks.txt", "w") as file:
                        file.writelines(lines)

                    print("Task Deleted. ✅")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye 👋")
        break

    else:
        print("Invalid Choice ❌")

        
