def strength(password):
    """
    Function to check if a given password is strong enough, it checks:
    If password is 8 or more chars, has at least one uppercase letter and one digit
    """

    result = {}
    if len(password) >= 8:
        result["length"] = True
    else: 
        result["length"] = False

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    result["upper-case"] = uppercase

    DIGIT = False
    for i in password:
        if i.isdigit():
            DIGIT = True
    result["digit"] = DIGIT

    if all(result.values()) is True:
        return "Strong Password"
    else:
        return "Weak Password"

print(strength("Password1"))