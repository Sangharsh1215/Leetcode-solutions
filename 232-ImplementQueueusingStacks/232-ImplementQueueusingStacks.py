# Last updated: 3/30/2025, 1:48:41 AM
class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        self.stack1.append(x)
        

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

        

    def empty(self):
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()