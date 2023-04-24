class My_Iterator:
    num_iter = 0

    def __init__(self, _from, _to, step = 1):
        if step <= 0 or _from > _to:
            raise ValueError ('such arguments are not suitable for creating an object')
        self._from = _from
        self.start = _from
        self._to = _to
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._from > self._to:
            raise StopIteration
        val = self._from
        self._from += self.step
        self.num_iter += 1
        return val

    def __getitem__(self, num):
        if num >= self.num_iter or num < 0:
            raise IndexError("Index out of range")
        current = self.start
        for i in range(num):
            current += self.step
        return current


c = My_Iterator(-3, 3, 2)
for i in c:
    print(i)
print('item', c[2])