class Deque:
    def __init__(self):
        self.data = []

    def add_front(self, value):
        self.data.insert(0, value)

    def add_rear(self, value):
        self.data.append(value)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


if __name__ == "__main__":
    d = Deque()
    d.add_front(10)
    d.add_rear(20)
    d.add_front(5)

    print(d.remove_front())
    print(d.remove_rear())
