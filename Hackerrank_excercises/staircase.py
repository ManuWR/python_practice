def staircase(n):
    for i in range(n):
         # Calculate the number of spaces needed for right alignment
        spaces = ' ' * (n - i - 1)
        print(spaces + (i + 1) * "#")
        #i+=1
        #print( i * "#")

n = 7

staircase(n)