import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a to-do')

input_box = sg.InputText(tooltip='Enter todo',key='entered todo item')
todos= []
list_box = sg.Listbox(values=todos,size=[40,20])

add_button = sg.Button(button_text='Add',size=[3,1])
edit_button = sg.Button('edit')
complete_button = sg.Button('complete')
exit_button = sg.Button('exit')
show_button =sg.Button('show')

window = sg.Window(title="My To-Do App",
                   layout =[
                                [label],
                                [input_box],
                                [list_box,
                                [add_button,edit_button,complete_button,show_button]],

                                [exit_button]
                            ],
                   font=('Tahoma',10))
while True:

    event,values = window.read()
    print(f"event = {event} ")
    print(f"value = {values}")

    match event:
        case 'Add':
            try:
                todo = values['entered todo item']
                print(todo)
                todos = functions.get_todos(functions.TODO_FILES_PAHT)
                todos.append(todo.capitalize() + '\n')  # the new todoo item is appended to list read from the file todos
                todos.sort(key=str.lower)


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
        case 'show':
            todos = functions.get_todos(functions.TODO_FILES_PAHT)
            new_todos = []
            new_todos = [todo_item.strip('\n') for todo_item in todos]  # list comprehension to contract the for lop in one line

            list_box.update(values=new_todos)
        case sg.WINDOW_CLOSED:
            break

window.close()