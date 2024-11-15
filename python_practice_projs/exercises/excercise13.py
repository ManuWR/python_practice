def get_nr_items(user_input):
    user_input = user_input.split(",")
    return len(user_input)

user_inp = input("Enter list separated by commas: ")
print(get_nr_items(user_inp))