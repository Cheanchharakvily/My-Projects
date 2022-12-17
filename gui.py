import Functions
import PySimpleGUI as gui

label = gui.Text("Enter your Text")
user_input = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button('Add')

List_Box = gui.Listbox(values=Functions.openfileread(), key="todos", enable_events=True, size=[45, 10])
edit_button = gui.Button('Edit')

window = gui.Window('To do App',
                            layout=[[label], [user_input, add_button], [List_Box, edit_button]],
                            font=('Helvetica', 12))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = Functions.openfileread()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            Functions.openfilewrite(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = Functions.openfileread()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            Functions.openfilewrite(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
