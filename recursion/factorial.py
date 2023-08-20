def factorial(n):
    assert n >= 0 and int(n) == n, 'Give me Number which is positive'
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(9))