import Functions
import PySimpleGUI as gui
import time

gui.theme('DarkBlue14')
clock = gui.Text('', key="clock")
label = gui.Text("Enter your Text")
user_input = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button('Add')

List_Box = gui.Listbox(values=Functions.openfileread(), key="todos", enable_events=True, size=(45, 10))
edit_button = gui.Button('Edit')
remove_button = gui.Button('Remove')

exit_button = gui.Button('Exit')

window = gui.Window('To do App',
                    layout=[[clock],
                            [label],
                            [user_input, add_button],
                            [List_Box, edit_button, remove_button],
                            [exit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%A, %d/%b/%Y, %H:%M:%S"))
    match event:
        case "Add":
            todos = Functions.openfileread()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            Functions.openfilewrite(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = Functions.openfileread()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                Functions.openfilewrite(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Select any todo first!", font=('Helvetica', 12))

        case "Remove":
            remove_todo = values['todos'][0]
            todos = Functions.openfileread()
            todos.remove(remove_todo)
            Functions.openfilewrite(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case gui.WIN_CLOSED:
            break

window.close()
