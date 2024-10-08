todos = []
# i = False
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            n = int(input("Number of ToDo to edit: "))
            n -= 1
            new_todo = input("Enter new todo: ")
            todos[n] = new_todo
        case 'complete':
            n = int(input("Number of the todo to complete: "))
            n-=1
            todos.pop(n)
        case 'exit':
            break
        case err:
            print("You entered an unknown command. Try again.")
print('Goodbye!')

"""while False:
    todo = input(prompt)
    print(todo)
    print("Next...")"""
