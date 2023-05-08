class StackNodes:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class StackList:

    def __init__(self):
        self.top = None
        self.counter = 0

    def output_list(self):
        current_node = self.top
        while current_node is not None:
            print(str(current_node.data)+' ', end = ' ')
            current_node = current_node.next
        print('')

    def push(self, data):
        node = StackNodes(data)
        if self.counter != 0:
            node.next = self.top
        self.top = node
        self.counter += 1

    def pop(self):
        if self.counter == 0:
            print('no nodes for delete')
        elif self.counter == 1:
            self.top = None
            self.counter = 0
            print('stack is empty')
        else:
            self.counter -= 1
            self.top = self.top.next
            
    def peak(self):
        if self.counter == 0:
            print('stack is empty')
            return None
        else:
            print('peak is', self.top.data)
            return self.top.data

    def isempty(self):
         return self.counter == 0

    def size(self):
         return self.counter

stack = StackList()
#print(stack.size())
#print(stack.isempty())
#stack.peak()
stack.push(3)
stack.output_list()
#stack.peak()
stack.push(5)
stack.output_list()
#stack.peak()
stack.push(7)
stack.output_list()
#print(stack.isempty())
stack.pop()
stack.output_list()
stack.pop()
stack.output_list()
#print(stack.size())