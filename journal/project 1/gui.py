import PySimpleGUI as sg
import functions

label = sg.Text("Enter to do ")
input_box = sg.InputText(tooltip="Enter todo list", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
windows = sg.Window('My-To-Do app', layout=[[label], [input_box, add_button],[list_box,edit_button]], font=('Helvetica', 20))

while True:
    event, value = windows.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo= value['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case "todos":
            windows['todo'].update(value=value['todos'][0])

windows.close()