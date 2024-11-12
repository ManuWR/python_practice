def get_max_min():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    mini = min(grades)
    message = f"Max: {maximum}, Min: {mini}"
    return message
    
max_min = get_max_min()
print(max_min)