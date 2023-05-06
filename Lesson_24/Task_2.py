class My_Stack():
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

def is_balanced (text):
    stack = My_Stack()
    opened = '({['
    closed = ')}]'
    for i in text:
        if i in opened:
            stack.push(i)
        elif i in closed:
            if stack.size() == 0:
                print('not balanced')
                return False
            elif opened[closed.index(i)] != stack.pop():
                print('not balanced')
                return False
    if stack.size() != 0:
        print('not balanced')
        return False
    else:
        print('balanced')
        return True


is_balanced ('{{d}(f[gh])}j')





