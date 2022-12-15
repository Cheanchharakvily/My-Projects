from Functions import openfileread, openfilewrite
import PySimpleGUI as gui

label = gui.Text("Enter your Text")
user_input = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button('Add')

window = gui.Window('To do App',
                            layout=[[label], [user_input, add_button]],
                            font=('Helvetica', 11))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = openfileread()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            openfilewrite(todos)
        case gui.WIN_CLOSED:
            break

    window.close()