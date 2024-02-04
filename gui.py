import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a to-do")
input_box = PySimpleGUI.InputText(tooltip="Enter To-Do", key='todo')
add_button = PySimpleGUI.Button("Add")

window = PySimpleGUI.Window("To-Do App",
                            layout=[[label], [input_box, add_button]],
                            font=('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case PySimpleGUI.WIN_CLOSED:
            break

window.close()
