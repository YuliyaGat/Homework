class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def get_from_stack(self):
        elist = []
        if len(self.stack) > 0:
            for i in range(len(self.stack)):
               elist.append(self.stack.pop())
            for j in reversed(elist):
               if j != 'e' and j != 'E':
                  self.stack.append(j)
        if 'e' not in elist and 'E' not in elist:
            raise ValueError('e is not found')
        return self

    def __str__(self):
            return f'Stack({self.stack})'
    def __repr__(self):
            return self.__str__()

def full_stack(text):
    stack = Stack()
    for i in text:
        stack.push(i)
    return stack

stack2 = Stack()
stack2.push('q')
stack2.push('w')
stack2.push('e')
stack2.push('r')
stack2.push('E')
print(stack2)
print(stack2.get_from_stack())

print(full_stack('Eqwerty'))
print(full_stack('Eqwerty').get_from_stack())




