#Task2 access a function inside a function (Tips: use function, which returns another function)

def outside_func(q,w):
    k = 5
    def sum_func(i, j): return i + j + k
    return sum_func(q,w)

print(outside_func(4,3))