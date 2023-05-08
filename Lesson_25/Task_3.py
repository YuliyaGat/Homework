class QueueNodes:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class QueueList:

    def __init__(self):
        self.head =None
        self.tail = None
        self.counter = 0

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.data) + ' ', end=' ')
            current_node = current_node.next
        print('')

    def enqueue(self, data):
        node = QueueNodes(data)
        if self.counter != 0:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.counter += 1

    def dequeue(self):
        if self.counter == 0:
            print('no nodes for delete')
        elif self.counter == 1:
            self.tail = None
            self.head = None
            self.counter = 0
            print('queue is empty')
        else:
            self.counter -= 1
            self.head = self.head.next

    def isempty(self):
        return self.counter == 0

    def size(self):
        return self.counter

queue = QueueList()
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


