n=3
arr=[
    [11, 2, 4], 
    [4, 5, 6], 
    [10, 8, -12]]

def diagonalDifference(arr):
    d = 0
    e = 0
    for i in range(n):
        d += arr[i][i]
        e += arr[i][n-i-1]
        i+=1
    return abs(d - e)

print(diagonalDifference(arr))