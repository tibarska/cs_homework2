class Stack:
    def __init__(self):
        self.lst = []
        self.size = len(self.lst)

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        return self.lst.pop()
