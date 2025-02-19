
todos= []
while True:
    user_action = (input("Type add, edit, show, complete or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
            todos.sort()
        case 'show'|'display':
            for  index, todo_item in enumerate(todos):
                print(f"{index+1}-{todo_item.capitalize()}")

        case 'edit':
            number = int(input(" number if the todo to edit: "))
            print(number)
            todo_to_be_edited = todos[number -1]
            print(todo_to_be_edited)
            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo
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

