def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with postive integers")
    elif n == 0:
        return 0
    else:
        rez = a + mult(a, n - 1)
        return rez




print(mult(3, 5))