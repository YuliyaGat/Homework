class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def get_from_queue(self):
        if 'e' not in self.queue and 'E' not in self.queue:
            raise ValueError('e is not found')
        else:
            while 'e' in self.queue:
                self.queue.pop(self.queue.index('e'))
            while 'E' in self.queue:
                self.queue.pop(self.queue.index('E'))
            return self

    def __str__(self):
            return f'Queue({self.queue})'
    def __repr__(self):
            return self.__str__()

def full_queue(text):
    queue = Queue()
    for i in text:
        queue.enqueue(i)
    return queue

queue2 = Queue()
queue2.enqueue('q')
queue2.enqueue('w')
queue2.enqueue('e')
queue2.enqueue('r')
queue2.enqueue('E')
print(queue2)
print(queue2.get_from_queue())

print(full_queue('Eqwerty'))
print(full_queue('Eqwerty').get_from_queue())




