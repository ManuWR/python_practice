arr = [1, 2, 3, 4, 5]

def miniMaxSum(arr):
    maxi = max(arr)
    arr.remove(maxi)
    min_sum = sum(arr)
    arr.append(maxi)
    arr.remove(min(arr))
    max_sum = sum(arr)
    print(min_sum, max_sum)

print(miniMaxSum(arr))
