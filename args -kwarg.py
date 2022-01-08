def func(x, *args):
    sum = 0
    for arg in args:
        sum += (x * arg)
    return sum
print(func(2,3,4,5))
