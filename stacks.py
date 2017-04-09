
"""
Stacks is a Linear Data Structure that can be accessed only
at one of its ends for either storing or retrieving.

LIFO         - Last In First Out

push         - Insert an item on the top of the stack.
pop          - Remove the item of the top of the stack.
top / peek   - Look up the element on the top.
empty / size - check whether the stack is empty or return its size.

"""


class Stacks(list):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, items):
        self.items.append(items)

    def pop(self, items):
        if not self.isEmpty():
            self.items.pop(items)
        else:
            raise Exception("Stack is empty..!")

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def main():
    stack = Stacks()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print stack.size()
    print stack.peek()
    print stack.pop(2)
    print stack.peek()


if __name__ == '__main__':
    main()
