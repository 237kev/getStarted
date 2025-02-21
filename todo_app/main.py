

while True:
#    user_action = (input("Type add, edit, show, complete or exit: ")).strip()
    user_action = (input("which action do you want to perform? ")).strip()


    if  user_action.startswith('add'):
        todos = []
        todo = (user_action[3:]).strip()
        with open("Files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo.capitalize() + '\n')      # the new todoo item is appended to list read from the file todos
        todos.sort(key=str.lower)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        with open("Files/todos.txt",'r') as file:
            todos = file.readlines()
        new_todos = []
        new_todos = [todo_item.strip('\n') for todo_item in todos] # list comprehension to contract the for lop in one line

        for index, todo_item in enumerate(new_todos):
            print(f"{index+1}-{todo_item.capitalize()}")


    elif user_action.startswith('edit'):
        try:
            with open("files/todos.txt", 'r') as file:
               todos = file.readlines()
            number = int((user_action[4: ]).strip())
            print(f"task {number} must be edited")
            todo_to_be_edited = todos[number -1]
            print(todo_to_be_edited)

            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo + '\n'

            with open("files/todos.txt", 'w') as file:
               file.writelines(todos)
               todos.sort(key=str.lower)
            print(new_todo)

        except ValueError:
            print("your command ist not valid")
            continue

    elif user_action.startswith('complete'):

        try:
            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            number = int( (user_action[8: ]).strip() )
            print("the " + str(number) + ". marked as completed")
            todo_to_be_edited = todos[number - 1]
            print(todo_to_be_edited + " has been completed \n und will be removed")
            todos.pop(number - 1)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
                todos.sort(key=str.lower)
        except ValueError:
            print("syntax error: task number expected after user action word 'complete' ")
        except IndexError:
            print("syntax error: task index is out if range ")
            continue


    elif user_action.startswith('exit'):
        break

    else: #"whatever" in user_action:
        print("you entered an unknown command")

print("bye!")

