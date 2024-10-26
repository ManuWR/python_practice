# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


s = 1
t = 10
a = 3
b = 4
apples = [3, 2, -1]
oranges = [4, 6, -3]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    """
    Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
    """
# Commented solution avoid to use rang to select from a range, according to Hackerank is a more effective solution.
    rang = range(s, t)
    apples_in_region = 0
    for i in apples:
        if i + a in rang:
        # if i + a >= s and i + a <= t:
            apples_in_region += 1

    oranges_in_region = 0
    for i in oranges:
        if i + b in rang:
        # if i + b >= s and i + b <=t:
            oranges_in_region += 1
    print(apples_in_region)
    print(oranges_in_region)


countApplesAndOranges(s, t, a, b, apples, oranges)