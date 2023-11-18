class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % len(self.queue)
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear - 1]
        

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.queue[self.front] == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.queue[self.front] != None:
            return True
        else:
            return False