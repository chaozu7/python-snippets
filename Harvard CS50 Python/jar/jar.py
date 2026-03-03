class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too much! Eat sth!")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("We don't have enough cookies!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 1:
            raise ValueError("Couldn't be less than 0")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Too much cookies")
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(10)
    print(jar)
    jar.withdraw(9)
    print(jar)


if __name__ == "__main__":
    main()
