class TypeDecorators:

    @staticmethod
    def to_int(func):
        def wraps(*args):
            return int(func(*args))
        return wraps

    @staticmethod
    def to_str(func):
        def wraps(*args):
            return str(func(*args))
        return wraps

    @staticmethod
    def to_bool(func):
        def wraps(*args):
            return bool(func(*args))
        return wraps

    @staticmethod
    def to_float(func):
        def wraps(*args):
            return float(func(*args))
        return wraps

@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

assert do_nothing('25') == 25
assert do_something('True') is True

