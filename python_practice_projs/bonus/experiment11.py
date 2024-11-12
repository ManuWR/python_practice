def greet():
    message = "hello"
    new_message = message.capitalize()
    print("Hey hey")
    return new_message # return None if nothing is returned

greeting = greet()
print(greeting)
print(len(greeting)) # Error if fucntion not return anything