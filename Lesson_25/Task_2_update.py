from Task_1 import *

class Stack:
    def __init__(self):
        self._item = UnorderedList()

    def output_list(self):
        return self._item.output_list()

    def push(self, data):
        self._item.append(data)

    def pop(self):
        return self._item.pop()
            
    def peak(self):
        if self._item.counter == 0:
            print('stack is empty')
            return None
        else:
            print('peak is', self._item.tail.data)
            return self._item.tail.data

    def isempty(self):
         return self._item.counter == 0

    def size(self):
         return self._item.counter

stack = Stack()
print(stack.size())
print(stack.isempty())
stack.peak()
stack.push(3)
stack.output_list()
stack.peak()
stack.push(5)
stack.output_list()
stack.peak()
stack.push(7)
stack.output_list()
print(stack.size())
print(stack.isempty())
stack.pop()
stack.output_list()
stack.pop()
stack.output_list()
print(stack.size())