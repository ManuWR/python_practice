user_prompt = "Enter a To Do:"
todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
