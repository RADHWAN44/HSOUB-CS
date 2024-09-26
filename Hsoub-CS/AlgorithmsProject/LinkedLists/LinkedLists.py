class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print('InLinkedList')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node



    def deleteNode(self, key):
        temp = self.head

        if (temp):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if (temp == None):
            return
        prev.next = temp.next
        temp = None












if __name__ == '__main__':
    list = LinkedList()
    list.head = Node(1)
    second = Node(2)
    third = Node(3)
    list.head.next = second
    second.next = third
    for i in range(10):
        list.append(i)
    list.deleteNode(8)
    list.printList()




