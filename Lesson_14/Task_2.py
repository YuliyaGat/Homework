def stop_words(words: list):
    def decorator(func):
        def wrapped(name):
            slogan = func(name)
            for i in range(len(words)):
                slogan = slogan.replace (str(words[i]), '*')
            return slogan
        return wrapped
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"