member = input("Add a new member: ") + "\n"

file = open("members.txt", "a")
file.write(member)
file.close()