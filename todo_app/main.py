

while True:
    try:

        user_action = (input("which action do you want to perform? ")).strip()


        if user_action.startswith('add'):
            try:
                todos = []
                todo = (user_action[3:]).strip()
                try:
                    with open("Files/todos.txt", 'r') as file:
                        todos = file.readlines()
                except FileNotFoundError:
                    todos = []  # Initialize an empty list if the file doesn't exist

                todos.append(todo.capitalize() + '\n')      # the new todoo item is appended to list read from the file todos
                todos.sort(key=str.lower)

                with open("files/todos.txt", 'w') as file:
                    file.writelines(todos)
            except AttributeError:
                print("Error: 'user_action' should be a string.")
            except ValueError as ve:
                print(f"Error: {ve}")
            except PermissionError:
                print("Error: Insufficient permissions to read/write the file.")
            except IsADirectoryError:
                print("Error: 'Files/todos.txt' is a directory, not a file.")
            except IOError as io_err:
                print(f"IO error occurred: {io_err}")
            except NameError:
                print("Error: 'user_action' is not defined.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


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
            except FileNotFoundError:
                print("Error: The file 'files/todos.txt' does not exist.")
                todos = []  # Initialize an empty list if the file doesn't exist

            try:
                number = int((user_action[4: ]).strip())
                if number < 1 or number > len(todos):
                 IndexError("The task number is out of range.")

            except ValueError:
                print("Error: Please provide a valid task number after 'edit'.")
            except IndexError as ie:
                print(f"Error: {ie}")
            else:
                print(f"Task {number} must be edited:")
                todo_to_be_edited = todos[number -1]
                print(todo_to_be_edited)

            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo + '\n'
            try:
                with open("files/todos.txt", 'w') as file:
                   file.writelines(todos)
                   todos.sort(key=str.lower)
                print(new_todo)
            except PermissionError:
                print("Error: Insufficient permissions to write to the file.")
            except IsADirectoryError:
                print("Error: 'files/todos.txt' is a directory, not a file.")
            except IOError as io_err:
                print(f"IO error occurred: {io_err}")



        elif user_action.startswith('complete'):

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            try:
                number = int(user_action[8:].strip())
                if number < 1 or number > len(todos):
                    raise IndexError("Die Aufgabennummer liegt außerhalb des gültigen Bereichs.")
            except ValueError:
                print("Fehler: Bitte geben Sie eine gültige Aufgabennummer nach 'complete' ein.")
            except IndexError as ie:
                print(f"Fehler: {ie}")
            else:
                print(f"Aufgabe {number} wurde als erledigt markiert:")
                todo_to_be_completed = todos[number - 1]
                print(f"{todo_to_be_completed.strip()} wurde abgeschlossen und wird entfernt.")
                todos.pop(number - 1)

            try:
                with open("files/todos.txt", 'w') as file:
                    file.writelines(todos)
                    todos.sort(key=str.lower)
            except PermissionError:
                print("Error: Insufficient permissions to write to the file.")
            except IsADirectoryError:
                print("Error: 'files/todos.txt' is a directory, not a file.")
            except IOError as io_err:
                print(f"IO error occurred: {io_err}")


        elif user_action.startswith(exit):
            break

        else: #"whatever" in user_action:
            print("you entered an unknown command")

    except NameError:
        print("Fehler: 'user_action' ist nicht definiert.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

print("bye!")

