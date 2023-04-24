# import itertools
#
# def with_index(iterable, start=0):
#     return zip(itertools.count(start), iterable)
#
def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield (start, iterable[i])
        start += 1

print(list(with_index([2,5,7],0)))
print(list(enumerate([2,5,7],0)))


