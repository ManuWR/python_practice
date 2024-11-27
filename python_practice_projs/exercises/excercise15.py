import random

# Get two numbers from the user and covert them to integers
low = int(input("Enter the lower bound: "))
up = int(input("Enter the upper bound: "))

# Pick a random int using randrange or randint
print(random.randrange(low +1, up))
print(random.randint(low +1, up))