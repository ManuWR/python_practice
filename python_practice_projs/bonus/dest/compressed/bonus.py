passw = input("Enter a password: ")
x = 1

while passw != "pass123" and x < 3:
    print("Incorrect password! Please try again: ")
    passw = input("Enter a password: ")
    x += 1

if passw == "pass123":
    print("Password was correct!")
else:
    print("Login denied!")
