class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int)->None:
        if len(self.stack1) == 0:
            return self.stack1.append(x)

        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()

    def empty(self):
        return True if len(self.stack1) == 0 else False

if __name__=='__main__':
    m = MyQueue()
    m.push(4)


