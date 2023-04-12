while True:
    user_action = input("Type add or show:").strip()
    i = 0
    match user_action:
        case 'add':
            todo = input("Give me your action:") + "\n"
            file = open('todos.txt','r')
            todos = file.readlines()
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()
            for item in todos:
                i=i+1
                print(i,item, end="")
        case 'edit':
            number = int(input("Which item you want to edit?"))
            new = input("What do you want to edit it with?")
            todos[number-1] = new
        case 'complete':
            name = input("Which item do you want to mark complete?")
            todos.remove(name)
        case 'exit':
            break

print("Bye!")
