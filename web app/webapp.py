import streamlit as sl
import functions

todos = functions.get_todos()
def add_todo():
    todo = sl.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
def remove_todo():
    for todo in todos:
        if sl.session_state[todo] == True:
            todos.remove(todo)
    functions.write_todos(todos)

sl.title("My to-do app")
sl.subheader("This is my to-do app")
sl.write("This app increase productivity")

todos = functions.get_todos()

for todo in todos:
    sl.checkbox(todo, key=todo, on_change=remove_todo)
sl.text_input(label="", placeholder="Add a to-do", on_change= add_todo , key="new_todo")
