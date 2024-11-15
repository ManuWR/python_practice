# def greet(message):
#     new_message = message.capitalize()
#     print("Hey hey")
#     return new_message # return None if nothing is returned

# user_entry = input("What greeting do you want? ")
# greeting = greet(user_entry)

# print(greeting)
# #print(len(greeting)) # Error if fucntion not return anything

# def speed(distance, time):
#     return distance / time

# print(speed(200, 4))

# string = "New drive"

# print(len(string))


def get_nr_items(user_input):
    user_input = user_input.split(",")
    return len(user_input)

user_inp = input("Enter list separated by commas: ")
print(get_nr_items(user_inp))