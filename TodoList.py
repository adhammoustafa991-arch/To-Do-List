my_Tasks = []

try:
    with open ("tasks.txt","r") as file :
        saved_Lines = file.readlines()

        for line in saved_Lines:
            clean_task = line.strip()
            my_Tasks.append(clean_task)
except FileNotFoundError :
    pass

while True : 
    print(" Main Menu. \n")
    print("1- add task")
    print("2- Show my current tasks")
    print("3- Quit. \n")

    user_choice = input('choose an option : ')

    if user_choice == '1' :
        new_task = input('Enter your tasks : ')
        my_Tasks.append(new_task)
        with open("tasks.txt", "w") as file:
            for task in my_Tasks:
                file.write(task + "\n")
    elif user_choice == '2':
        print(f'Here is your tasks : {my_Tasks}')
    elif user_choice == '3':
        with open("tasks.txt", "w") as file:
            for task in my_Tasks:
                file.write(task + "\n")
        print('shutting down todo list')
        break
    else :
        print('invalid option, please put valide one.')



