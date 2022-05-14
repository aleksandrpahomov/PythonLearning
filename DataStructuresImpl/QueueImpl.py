class FIFO():
    def __init__(self):
        self.Queue = []

    def put(self, value):
        self.Queue.append(value)

    def get (self):
        return self.Queue.pop(0)

myQueue = FIFO()
myQueue.put(1)
myQueue.put(2)

print(myQueue.get())