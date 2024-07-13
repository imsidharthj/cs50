class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity is not a non-negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"
    
    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("exceeds capacity")
        elif self._size + n > self._capacity:
            raise ValueError("Exceeds capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("less cookies in jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

cookies = Jar()
cookies.deposit(11)
cookies.withdraw(1)
print(cookies)