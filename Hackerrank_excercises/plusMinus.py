def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            p += 1
        elif arr[i] < 0:
            n += 1
        else:
            z += 1
    for i in p, n, z:
        #print(i/len(arr))
        print(round(i/len(arr), 6))

arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)