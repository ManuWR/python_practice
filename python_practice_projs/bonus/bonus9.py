password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else: 
    result["length"] = False

DIGIT = False
for i in password:
    if i.isdigit():
        DIGIT = True

result["digit"] = DIGIT

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["upper-case"] = uppercase

# print(result)
# print(result.values())

#if all(result):
if all(result.values()) is True:
    print("Strong password")
else:
    print("Weak password")