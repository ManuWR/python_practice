# i = False
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        # continue

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

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
        # Method 3: modifying item directly to remove blank space here:
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        n = int(user_action[5:])
        n -= 1
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[n] = new_todo + '\n'
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        n = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        n -= 1
        # todo_to_remove = todos[n].strip('\n')
        # todos.pop(n)
        todo_to_remove = todos.pop(n).strip('\n')

        with open("todos.txt", "w") as file:
            file.writelines(todos)
        
        print(f"Todo {todo_to_remove} was removed from the list.")

    elif 'exit' in user_action:
        break
    else:
        print("Command not valid. Please try again.")
print('Goodbye!')

"""while False:
    todo = input(prompt)
    print(todo)
    print("Next...")"""
