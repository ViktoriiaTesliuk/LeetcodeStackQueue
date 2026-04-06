class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, x):
        new_node = Node(x)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def pop(self):
        if self.is_empty():
            return None
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.front.val

    def is_empty(self):
        return self.front is None

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
