def sumofn(num):
    if num==1:
        return 1
    else:
        return num + sumofn(num-1)
print(sumofn(6))