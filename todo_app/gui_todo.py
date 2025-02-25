import functions
import FreeSimpleGUI as sg

print(f"Executable Path: {functions.TODO_FILES_PATH}")

sg.theme('Black')

label = sg.Text('Type in a to-do')

input_box = sg.InputText(tooltip='Enter todo',key='entered todo item', background_color='Grey')
todos= []
list_box = sg.Listbox(values=todos,size=[40,20], key='-LIST-',enable_events=True)

add_button = sg.Button(button_text='Add',size=[3,1],bind_return_key=True)
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
                todos = functions.get_todos(functions.TODO_FILES_PATH)
                if todo not in todos:
                    todos.append(todo + '\n')  # the new todoo item is appended to list read from the file todos
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
            functions.set_todos(functions.TODO_FILES_PATH, todos)
            list_box.update(values=todos)

        case 'show':
            todos = functions.get_todos(functions.TODO_FILES_PATH)
            new_todos = []
            new_todos = [todo_item.strip('\n') for todo_item in todos]  # list comprehension to contract the for lop in one line

            list_box.update(values=new_todos)
        case sg.WINDOW_CLOSED:
            break
        case 'complete':
            todos = functions.get_todos(functions.TODO_FILES_PATH)
            clean_todos = [todo.strip() for todo in todos]
            selected_item = values['-LIST-']
            print(f"selected_item: {selected_item}")
            clean_todos.remove((selected_item[0]).strip())
            todos_with_newline = [todo + '\n' for todo in clean_todos]
            functions.set_todos(functions.TODO_FILES_PATH,todos_with_newline)
            list_box.update(values=todos_with_newline)
            input_box.update('')

        case'edit':
            try:
                todos = functions.get_todos(functions.TODO_FILES_PATH)
                selected_item = values['-LIST-']

                print(f"selected item: {selected_item}")
                new_todo = values['entered todo item']
                clean_todos = [todo.strip('\n') for todo in todos]
                index_of_selected_item = clean_todos.index((selected_item[0]).strip())
                clean_todos[index_of_selected_item] = new_todo
                clean_todos.sort(key=str.lower)
                list_box.update(values=clean_todos)
            except ValueError:
                print("Error: Selected item not found in the list.")
                sg.popup("Error: Selected item not found in the list.")
            except IndexError:
                sg.popup("Error: select a todo first")
            except NameError:
                sg.popup("Error: select a todo first")




            todos_with_newline = [todo + '\n' for todo in clean_todos]
            functions.set_todos(functions.TODO_FILES_PATH, todos_with_newline)

        case'-LIST-':
            selected_item = values['-LIST-']
            window['entered todo item'].update(selected_item[0])




window.close()