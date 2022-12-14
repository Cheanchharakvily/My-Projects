def openfileread(filepath='Files/todos.txt'):
    """Open read file and return file value"""
    with open(filepath, 'r') as file:
        todosread = file.readlines()
    return todosread


def openfilewrite(todo_arg, filepath='Files/todos.txt'):
    """Open and write value in file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)
