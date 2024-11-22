# from functions import get_todos, write_todos
import functions

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith(("add","new")):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos("todos.txt")

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
    elif user_action.startswith("edit"):
        try:
            n = int(user_action[5:])
            n -= 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[n] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            n = int(user_action[9:])
            todos = functions.get_todos()
            
            n -= 1
            # todo_to_remove = todos[n].strip('\n')
            # todos.pop(n)
            todo_to_remove = todos.pop(n).strip('\n')

            functions.write_todos(todos)
            
            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid. Please try again.")
print('Goodbye!')

"""while False:
    todo = input(prompt)
    print(todo)
    print("Next...")"""
