# var, var1, var2 = 1,2,3
# print(var)
# print(var1,var2,)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)