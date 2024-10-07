def timeConversion(s):
    hh = int(s[0:2])
    if "PM" in s:
       if hh != 12:
           hh += 12
    else:
        if hh == 12:
            hh -= 12
        hh = "0" + str(hh)
        
    t = str(hh) + s[2:8]
    return t

s = "07:05:45PM"
#s= "12:40:03AM"

print(timeConversion(s))