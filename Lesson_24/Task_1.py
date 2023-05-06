class My_Stack:
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

def my_reverse(text):
    stack_reverse = My_Stack()
    for i in text:
        stack_reverse.push(i)
    text_reverse = ''
    for j in range(stack_reverse.size()):
        text_reverse = text_reverse + stack_reverse.pop()
    return text_reverse

print(my_reverse('Hello! It is a nice day.'))














