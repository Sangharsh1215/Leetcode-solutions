# Last updated: 3/31/2025, 4:44:43 PM
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val < self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])


        

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

        

    def top(self):
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        if self.minstack:
            return self.minstack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()