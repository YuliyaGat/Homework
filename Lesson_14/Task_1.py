def logger(func):
    def wrapped(*args):
        text = func.__name__+' called with '
        for i in args:
            text += str(i) + ', '
        print(text[:-2])
        #rez = func(*args)
        #return rez
    return wrapped


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(7)