# a = []
# def push(a, z):
#     return a.append(z)
#
# def pop(a):
#     return a.pop()
#
# def pick(a):
#     return a[-1]
#
# def isempty(a):
#     return not bool(a)
#
# def size(a):
#     return len(a)
#
# push(a, 5)
# push(a, 7)
# #pop(a)
# print(pick(a))
# print(a)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def pick(self):
        return self.stack[-1]

    def isempty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)



stack = Stack()
stack.push(3)
stack.push(6)
print(stack.stack)
print(stack.pick())
# stack.pop()
# print(stack.stack)


