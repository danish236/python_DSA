def fibo(n):
    assert n >= 0 and int(n) == n, 'Error: Please input positive integer'
    if n in [0,1]:
        return n
    else:
        var= fibo(n-1) + fibo(n-2)
        return var
print(fibo(9))