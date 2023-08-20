def recursivemethod(n):
    if n < 2:
        print("N is less than 2")
    else:
        recursivemethod(n-1)
        print(n)
recursivemethod(10)