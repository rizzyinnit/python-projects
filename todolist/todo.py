tasks = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose: ")
    if choice == "1":
        task = input("add a task:")
        print (task, "is added")
        tasks.append(task)
    elif choice == "2":
            for task in tasks:
                print(task)

    elif choice == "3":
        remove = int(input("Which task do you want to remove? "))
        tasks.pop(remove - 1)
        print("Task removed.")

    elif choice == "4":
        break

