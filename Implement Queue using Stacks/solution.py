class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        if self.is_empty():
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def is_empty(self):
        return self.head is None

class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def _transfer(self):
        while not self.in_stack.is_empty():
            self.out_stack.push(self.in_stack.pop())

    def pop(self) -> int:
        if self.out_stack.is_empty():
            self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack.is_empty():
            self._transfer()
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.push(x)

        while not self.q1.is_empty():
            self.q2.push(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()
