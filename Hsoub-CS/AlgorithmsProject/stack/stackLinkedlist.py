class StackNode:


    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:


    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print("%d pushed to stack" % (data))

    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data


    def dispaly(self):
        test = self.root
        while (test):
            print(test.data)
            test = test.next




stack = Stack()
print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)

print("%d popped from stack" % (stack.pop()))
print("%d popped from stack" % (stack.pop()))
print("Top element is %d " % (stack.peek()))



print(stack.isEmpty())