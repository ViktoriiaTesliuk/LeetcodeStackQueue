from collections import deque

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        f = self.freq[val]
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.groups:
            self.groups[f] = deque()
        self.groups[f].append(val)

    def pop(self) -> int:
        val = self.groups[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return val
