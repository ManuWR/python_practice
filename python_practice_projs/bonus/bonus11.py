def get_average():
    with open("../files/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(value) for value in values]

    avrg_local = sum(values) /len(values)
    return avrg_local


avrg = get_average()
print(avrg)