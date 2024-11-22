feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet,inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
# print("fi", f, i)
result = convert(f, i)

print(f"{f} feet and {i} is equal to {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can go to the game")