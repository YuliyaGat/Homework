import random
list_id = []
def unique_id():
    id_ = random.randint(1, 100000)
    while id_ in list_id:
        id_ = random.randint(1, 100000)
    list_id.append(id_)
    return id_

class Boss:

    def __init__(self, name: str, company: str):
        self.id = unique_id()
        self.name = name
        self.company = company
        self.workers = []

    #def get_add_worker(self):
    #    return self.workers

    def set_add_worker(self, new_worker):
        if isinstance(new_worker, Worker):
           self.workers.append(new_worker)
        else:
           raise ValueError('the new value is not in Worker')
        return self.workers

    def remove_worker(self, worker):
        if not isinstance(worker, Worker):
           raise ValueError('the new value is not in Worker')
        if worker in self.workers:
           self.workers.remove(worker)
        return self.workers

    def __str__(self):
        return f'Boss({self.id}, {self.name}, {self.company})'
    def __repr__(self):
        return self.__str__()

class Worker:

    def __init__(self, name: str, boss: Boss):
        self.id = unique_id()
        self.name = name
        self._boss = boss
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss_):
        if not isinstance(new_boss_, Boss):
            raise ValueError('the new value is not in Boss')
        self._boss.remove_worker(self)
        self._boss = new_boss_
        new_boss_.set_add_worker(self)

    def __str__(self):
        return f'Worker({self.id}, {self.name}, {self._boss})'
    def __repr__(self):
        return self.__str__()

a = Boss('Bill Brown', 'MD')
b = Boss('Glenn Scott', 'Disney')
c = Boss('Michael Grey', 'WB')
aa = Worker('Anton', a)
bb = Worker('Vadim', b)
cc = Worker('Sergey', c)
print(aa.boss)
print(aa)
aa.boss = b
cc.boss = a
print(aa)
print(a.workers)
print(b.workers)
print(c.workers)
