
def get_todos():

    with open('todo', 'r') as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(todos_argv):

    with open('todo','w') as file:
        file.writelines(todos_argv)
if __name__ == "__main__":
    print("Hello")
