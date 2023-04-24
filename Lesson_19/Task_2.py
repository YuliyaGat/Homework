def in_range(start, end, step):
    if step == 0:
        raise ValueError ('range() arg 3 must not be zero')
    else:
        i = start
        while i < end and step > 0 or i > end and step < 0 :
            yield i
            i += step

print(list(in_range(-10,-20,-3)))
print(list(range(-10,-20,-3)))

#print(in_range(2,10,3))
#print(range(2,10,3))