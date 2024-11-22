from parsers14 import parse
from converters14 import convert

feet_inches = input("Enter feet and inches: ")


f, i = parse(feet_inches)
# print("fi", f, i)
result = convert(f, i)

print(f"{f} feet and {i} is equal to {result}")

if result < 1:
    print("Kid is too small")
else:
    print("Kid can go to the game")