import functions

while True:
    try:
        user_action = (input("which action do you want to perform? ")).strip()
        if user_action.startswith('add'):
            try:
                todos = []
                todo = (user_action[3:]).strip()

                todos = functions.get_todos(functions.TODO_FILES_PAHT)
                todos.append(todo.capitalize() + '\n')      # the new todoo item is appended to list read from the file todos
                todos.sort(key=str.lower)

                functions.set_todos(functions.TODO_FILES_PAHT, todos)
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
            functions.set_todos(functions.TODO_FILES_PAHT, todos)

        elif user_action.startswith('show'):
            todos = functions.get_todos(functions.TODO_FILES_PAHT)
            new_todos = []
            new_todos = [todo_item.strip('\n') for todo_item in todos] # list comprehension to contract the for lop in one line

            for index, todo_item in enumerate(new_todos):
                print(f"{index+1}-{todo_item.capitalize()}")

        elif user_action.startswith('edit'):
            todos = functions.get_todos(functions.TODO_FILES_PAHT)
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

            functions.set_todos(functions.TODO_FILES_PAHT,todos)


        elif user_action.startswith('complete'):

            todos = functions.get_todos(functions.TODO_FILES_PAHT)
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
                functions.set_todos(functions.TODO_FILES_PAHT,todos)
            except PermissionError:
                print("Error: Insufficient permissions to write to the file.")
            except IsADirectoryError:
                print("Error: 'files/todos.txt' is a directory, not a file.")
            except IOError as io_err:
                print(f"IO error occurred: {io_err}")


        elif user_action.startswith('exit'):
            break

        else: #"whatever" in user_action:
            print("you entered an unknown command")

    except NameError:
        print("Fehler: 'user_action' ist nicht definiert.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

print("bye!")

