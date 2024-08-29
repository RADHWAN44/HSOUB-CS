class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node, new_data):
        if prev_node == None:
            raise ValueError
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node


    def delete(self, index):
        if self.head is None:
            return
        item = self.head
        if index == 0:
            self.head = item.next
            del item
            return

        for i in range(index -1):
            item = item.next
            if item is None:
                break
        next_node = item.next.next
        del item.next
        item.next = next_node



    def print_list(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next

list = LinkedList()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

list.head = n1

list.head.next = n2
n2.next = n3

list.push(0)


list.delete(2)
list.print_list()
