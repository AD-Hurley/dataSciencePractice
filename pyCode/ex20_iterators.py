class Fibonacci():
    def __init__(self, limit):
        self.prev = 0
        self.next = 1
        self.n = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        if self.n <= self.limit:
            self.next = self.prev + self.next
            self.prev = self.next - self.prev
            return self.prev
        else:
            raise StopIteration

fibNum = Fibonacci(8)
itr=iter(fibNum)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break