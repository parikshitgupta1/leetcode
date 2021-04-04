class MyCircularQueue:
    
    def __init__(self, k: int):
        self.queue = list()
        self.max_size = k
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue.pop(0)
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) >= self.max_size
