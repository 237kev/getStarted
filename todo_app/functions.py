import sys
import os

# Get the directory where the EXE is located

#TODO_FILES_PATH = "Files/todos.txt"
#TODO_FILES_PATH = "C:\\Projekte\\Python\\getStarted\\todo_app\\todos.txt"


TODO_FILES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.txt")



def get_todos(path: str) -> list[str] :
    """
    Reads a text file containing a list of to-do items and returns them as a list of strings.

    Each item is assumed to be on a separate line in the file.

    :param path: The file path to read from.
    :return: A list of to-do items (each as a string).
    """
    try:
        if not os.path.exists(TODO_FILES_PATH):
            with open(TODO_FILES_PATH, "w") as file:
                file.write("")  # Write an empty string (optional)
        with open(TODO_FILES_PATH, 'r') as file:
            todos = file.readlines()
            return todos
    except FileNotFoundError:
            print("Error: The file 'files/todos.txt' does not exist.")
            todos = []  # Initialize an empty list if the file doesn't exist

def set_todos(path: str, todos: []):
    """
    Writes a list of to-do items to a text file, overwriting existing content.

    The items are sorted alphabetically before being written to the file.

    :param path: The file path to write to.
    :param todos: A list of to-do items to be saved.
    :return: None
    """
    try:
        with open(TODO_FILES_PATH, 'w') as file:
            todos.sort(key=str.lower)
            file.writelines(todos)
    except FileNotFoundError:
        print("Error: The file 'files/todos.txt' does not exist.")
    except PermissionError:
        print("Error: Insufficient permissions to write to the file.")
    except IsADirectoryError:
        print("Error: 'files/todos.txt' is a directory, not a file.")
    except IOError as io_err:
        print(f"IO error occurred: {io_err}")


print("Hello from function")