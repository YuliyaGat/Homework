from Task_1 import *

class Queue:
    def __init__(self):
        self._item = UnorderedList()

    def output_list(self):
        return self._item.output_list()

    def enqueue(self, data):
        self._item.append(data)

    def dequeue(self):
        return self._item.pop(0)

    def isempty(self):
         return self._item.counter == 0

    def size(self):
         return self._item.counter

queue = Queue()
print(queue.isempty())
print((queue.size()))
queue.enqueue(3)
queue.output_list()
queue.enqueue(5)
queue.output_list()
queue.enqueue(7)
queue.output_list()
print(queue.isempty())
print((queue.size()))
queue.dequeue()
queue.output_list()
queue.dequeue()
queue.output_list()


