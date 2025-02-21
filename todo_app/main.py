

while True:
    user_action = (input("Type add, edit, show, complete or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos = []
            with open("Files/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')      # the new todoo item is appended to list read from the file todos
            todos.sort(key=str.lower)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show'|'display':#

            with open("Files/todos.txt",'r') as file:
                todos = file.readlines()
            new_todos = []
            new_todos = [todo_item.strip('\n') for todo_item in todos] # list comprehension to contract the for lop in one line

            for  index, todo_item in enumerate(new_todos):
                print(f"{index+1}-{todo_item.capitalize()}")

        case 'edit':
            with open("files/todos.txt", 'r') as file:
               todos = file.readlines()
            number = int(input(" number if the todo to edit: "))
            print(number)

            todo_to_be_edited = todos[number -1]
            print(todo_to_be_edited)

            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo + '\n'

            with open("files/todos.txt", 'w') as file:
               file.writelines(todos)
               todos.sort(key=str.lower)





            print(new_todo)

        case 'complete':
            number = int(input("Enter the number of the completed todo: "))
            a = todos.pop(number - 1)
            print(f"{number + 1 } todo which is: has been completed")

        case 'exit':
            break

        case whatever:
            print("you entered an unknown command")

print("bye!")

