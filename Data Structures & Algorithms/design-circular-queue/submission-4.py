# thoughts:
# - use an array of size k internally - pre-allocate
# - keep track of head and tail/size

class MyCircularQueue:
    # Note: not thread-safe

    def __init__(self, k: int):
        self.array = [0] * k
        self.head = 0
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.array[(self.head + self.size) % len(self.array)] = value
        self.size += 1

        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.array[self.head] = 0
        self.head = (self.head + 1) % len(self.array)
        self.size -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[self.head]        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.array[(self.head + self.size - 1) % len(self.array)]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.array)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()