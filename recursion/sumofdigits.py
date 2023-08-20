def sumofdigits(n):
    assert n >= 0 and int(n)==n, 'Input positive integer only'
    if n == 0:
        return n
    else:
        sum = int(n%10) + sumofdigits(n//10)
        return sum
print(sumofdigits(212))