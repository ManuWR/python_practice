def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
    
print(water_state(1))

def termo(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <=25:
        return "Warm"
    else:
        return "Cold"