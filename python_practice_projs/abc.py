files = ["a.txt", "b.txt", "c.txt"]

for f in files:
    file = open(f"files/{f}", "r")
    cont = file.read()
    file.close()
    print(cont)