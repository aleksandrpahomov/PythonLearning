class Node:
    def __init__(self,value = None):
        self.data_value = value
        self.next_value = None

class SingleLinkedList:
    def __init__(self):
        self.head_value = None

    def push_front(self, new_data):
        new_node = Node (new_data)
        new_node.next_value = self.head_value
        self.head_value = new_node

    def push_back(self,new_data):
        new_node = Node(new_data)
        if self.head_value is None:
            self.head_value = new_node
            return
        last = self.head_value
        while last.next_value is not None:
            last = last.next_value
        last.next_value = new_node()
    def print_list(self):
        curr_value = self.head_value
        while curr_value is not None:
            print(curr_value)
            curr_value = curr_value.next_value









class LLInterface:
    def __init__(self):
        self.linked_list = SingleLinkedList()
    def convert (self, iterable):
        self.linked_list.head_value = Node(iterable[0])
        nodes = [Node(value) for value in iterable]
        for index, node in enumerate(nodes):
            if index == 0:
                self.linked_list.head_value = node
            if index< len(nodes) - 1:
                node.next_value = nodes[index+1]


    def print(self):
        self.linked_list.print_list()
    def add_left (self, value):
        self.linked_list.push_front(value)
    def add_right (self, value):
        self.linked_list.push_back(value)


ll_int = LLInterface()
ll_int.convert([1,2,3,4])