from Functions import openfileread, openfilewrite
import time

time = time.strftime("%A, %d/%b/%Y, %H:%M:%S")
print("Today is", time)

while True:
    user_action = input("add or show or edit or exit ")
    user_action = user_action.strip()
    user_action = user_action.casefold()

    if user_action.startswith('add'):
        Todo = user_action[4:]

        todos = openfileread()

        todos.append(Todo + '\n')

        openfilewrite(todos)

    elif user_action.startswith('show'):

        todos = openfileread()

        for index, item in enumerate(todos):
            # remove \n in the code
            item = item.strip('\n')
            # format string for row
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = openfileread()

            new_todo = input("Enter what to edit: ")
            todos[number] = new_todo + '\n'

            openfilewrite(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[7:])

            todos = openfileread()

            remove_todos = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            openfilewrite(todos)

            message = f"{remove_todos} was removed."
            print(message)
        except IndexError:
            print("The number is not found.")
            continue
        except ValueError:
            print("after remove write number to remove.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not founds")
