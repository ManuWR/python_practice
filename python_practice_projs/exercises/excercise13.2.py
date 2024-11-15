def temperature_check(temperature):
    check = False
    if temperature > 7:
        check = True
    return "Warm" if check is True else "Cold"

print(temperature_check(8))
print(temperature_check(7))