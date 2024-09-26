class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None

        return str(temp.data)

    def display(self):
        temp = self.front
        if self.isEmpty():
            print('Is Empty')
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.display()
    q.DeQueue()
    q.DeQueue()
    q.display()
