class Node:
    def __init__(self, value = None):
        self.previous = None
        self.next = None
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.head.previous =new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def push_back(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node
            new_node.previous = last
        self.size += 1

    def insert(self,value, index):
        if index > self.size - 1:
            raise ValueError("index out of range")
        if index == self.size:
            self.push_back(value)
            return
        if index == 0:
            self.push_front(value)
            return
        new_node = Node(value)
        insert_after_node = self.head
        for i in range(index-1):
            insert_after_node = insert_after_node.next
        new_node.next = insert_after_node.next
        insert_after_node.next = new_node
        new_node.prev = insert_after_node
        self.size += 1

    def print_list(self):
        if self.head is not None:
            curr_node =self.head
            while curr_node is not None:
                print(curr_node.value)
                curr_node=curr_node.next
        else:
            print("No elements")

my_list = DoubleLinkedList()
my_list.push_front(2)
my_list.push_front(3)
my_list.push_front(4)
my_list.insert(5,2)
my_list.print_list()