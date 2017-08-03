
class Nodes(object):

    def __init__(self, value=None):
        self.value = value
        self.items = []


class StackWithNodes(object):

    def __init__(self, ):
        self.top = None

    def isEmpty(self, ):
        return bool(self.top)

    def pop(self, ):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise Exception("Stack is empty..!")

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def size(self, ):
        node = self.top
        if node is not None:
            num_nodes = 1
        else:
            return 0
        node = node.next
        while node:
            num_node = 
