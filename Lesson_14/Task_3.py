def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapped(name):
            if type(name) != str:
                print('type is not string')
                return False
            else:
                cont = ''
                for i in contains:
                    if i not in name:
                       cont = cont + i + " "
                if len(name)>15:
                    print('max_lenght > 15')
                if cont != '':
                    print(cont + 'not contains')
                if cont != '' or len(name)>15:
                    return False
                else:
                    return func(name)
        return wrapped
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'