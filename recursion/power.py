def power(num1):
    assert num1 >= 0 and int(num1)==num1, 'Give me positive number'
    if num1 == 0:
        return 1
    else:
        pow = power(num1-1)
        return pow * 2
print(power(6))