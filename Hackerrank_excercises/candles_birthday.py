# This code exceed time limit (because it checks the max value anytime and compare)
""" def birthdayCakeCandles(candles):
    c = 0
    for i in range(len(candles)):
        if candles[i] == max(candles):
            c+=1
    return c """

# This code is more efficient because max value is stored before.
def birthdayCakeCandles(candles):
    c = 0
    maxi = max(candles)
    for i in candles:
        if i == maxi:
            c+=1
    return c

candles = [3, 1, 2, 3, 2]

print(birthdayCakeCandles(candles))