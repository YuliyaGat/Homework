def to_power(x, exp):
    if exp > 0:
        rez = x * to_power(x, exp-1)
        return rez
    else:
        return 1

print (to_power(2,3))