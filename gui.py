from Functions import openfileread, openfilewrite
import PySimpleGUI

label = PySimpleGUI.Text("Enter your Text")
user_input = PySimpleGUI.InputText()
add_button = PySimpleGUI.Button('Add')

window = PySimpleGUI.Window('To do App', layout=[[label], [user_input, add_button]])
window.read()
window.close()