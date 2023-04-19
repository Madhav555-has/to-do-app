import PySimpleGUI as sg
import functions
import time

sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text("Enter to do ")
input_box = sg.InputText(tooltip="Enter todo list", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
windows = sg.Window('My-To-Do app', layout=[[clock],[label], [input_box, add_button],[list_box,edit_button,exit_button],[complete_button]], font=('Helvetica', 20))

while True:
    event, value = windows.read(timeout=1000)
    windows["clock"].update(value=time.strftime("%b %d %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo= value['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                windows['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first")

        case "todos":
            windows['todo'].update(value=value['todos'][0])
        case "Exit":
            exit()
        case "Complete":
            try:
                todo_to_remove = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                windows['todos'].update(values=todos)
                windows['todo'].update(value="")
            except IndexError:
                sg.popup("Select an item first")
        case sg.WIN_CLOSED:
            break
windows.close()