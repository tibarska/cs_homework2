class Stack:
    def __init__(self):
        self.lst = []
        self.size = len(self.lst)

    def push(self, val):
        self.lst.append(val)

    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return

    def is_empty(self):
        return self.size > 0


if __name__ == '__main__":
    st = Stack()
    st.push(2)
    assert st.is_empty() == False
    assert st.pop() == 2
