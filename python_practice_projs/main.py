# i = False
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a ToDo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
            continue
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # Remove the blank space for each item
            # METHOD 1: Loop
            # new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            # METHOD 2: List comprehension
            # Need to change enumerate(new_todos) to only "todos"
            # new_todos = [item.strip('\n') for item in todos]

            
            for index,item in enumerate(todos):
            #Method 3: modifying item directly to remove blank space here:
                item = item.strip('\n')
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
