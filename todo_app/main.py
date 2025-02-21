

while True:
    user_action = (input("Type add, edit, show, complete or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")

            file = open("Files/todos.txt", "r")  # the file name todoo opened in write mode
            todos = file.readlines()       # the inhalt ist ausgelesen und ist stored in the list named todos
            file.close()



            todos.append(new_todo + '\n')      # the new todoo item is appended to list read from the file todos
            todos.sort(key=str.lower)

            file = open("files/todos.txt", "w")  # a new file is created in write mode and the old one does not exist anymore becuase it is now overwritten
            file.writelines(todos)         #the new list ist now written in the new created todos file with the new appended todoo item
            file.close()

        case 'show'|'display':#
            file = open("files/todos.txt", 'r')
            todos = file.readlines()
            file.close()

            new_todos = []
 #           for todo_item in todos:
 #               new_todo = todo_item.strip('\n')  # to remove the back slash by each item of the list
 #               new_todos.append(new_todo)

            new_todos = [todo_item.strip('\n') for todo_item in todos] # list comprehension to contract the for lop in one line

            for  index, todo_item in enumerate(new_todos):
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

