class Nodes:

    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.counter = 0

    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.data)+' ', end = ' ')
            current_node = current_node.next
        print('')

    def append(self, data):
        node = Nodes(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.counter += 1
        self.tail = node

    def pop(self, index = None):
        if index == None:
            index = self.counter-1
        if self.counter == 0:
            raise IndexError('the list is empty')
        elif index < 0 or index >= self.counter:
            raise IndexError ('the index is outside the boundaries of the list')
        else:
            current_id = 0
            current_node = self.head
            previous_node = None
            while current_node is not None:
                if current_id == index:
                    if previous_node is not None:
                        previous_node.next = current_node.next
                    else:
                        self.head = current_node.next
                previous_node = current_node
                current_node = current_node.next
                current_id = current_id + 1
            self.counter -= 1

    def insert(self, index, data):
        node = Nodes(data)
        if index <= 0:
            node.next = self.head
            self.head = node
        else:
            if index > self.counter:
                index = self.counter
            current_id = 0
            current_node = self.head
            previous_node = None
            while current_node is not None and current_id < index:
                previous_node = current_node
                current_node = current_node.next
                current_id += 1
            node.next = current_node
            previous_node.next = node
            self.counter += 1

    def index(self, data):
        index = 0
        k = 0
        current_node = self.head
        while current_node is not None:
            index += 1
            if current_node.data == data:
                k = 1
                return index
            current_node = current_node.next
        if k == 0:
            raise ValueError ('there is no data in list')

    def slice(self, start, stop):
        copylist = UnorderedList()
        current_node = self.head
        current_id = 0
        while current_node is not None:
            if current_id >= start and current_id < stop:
                copylist.append(current_node.data)
            current_node = current_node.next
            current_id += 1
        return copylist.output_list()

if __name__ == "__main__":
    a = UnorderedList()
    a.output_list()
    a.append(3)
    a.output_list()
    a.append(6)
    a.output_list()
    a.append(23)
    a.output_list()
    #print(a.index(3))
    #print(a.counter)
    a.pop(2)
    a.output_list()
    a.insert(1,44)
    a.output_list()
    a.insert(-0,4)
    a.output_list()
    a.slice(0,3)
    a.pop(2)
    a.output_list()



