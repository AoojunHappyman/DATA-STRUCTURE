class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print(s.pop())
    print(s.peek())
