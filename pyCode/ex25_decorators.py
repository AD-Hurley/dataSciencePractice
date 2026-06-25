def isArgPositive(func):
    def inner(x):
        if x < 0 or type(x) != int:
            raise Exception("Error: Negative or non-integer arguments")
        else:
            return func(x)
    return inner

@isArgPositive
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(10))