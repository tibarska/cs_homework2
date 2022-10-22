class Stack:
    def __init__(self):
        self.lst = []
        self.size = len(self.lst)

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        if self.size > 0:
            return self.lst.pop()
        else:
            return
    def is_empty(self):
        return self.size > 0
