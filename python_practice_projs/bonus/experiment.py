with open("../files/doc.txt", "r") as file:
    # With this line, it gets saturated and trying to read the file again, returns an empty output.
    # file.read()
    content = file.read()

print(content)