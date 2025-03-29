# Last updated: 3/30/2025, 1:36:11 AM
class MyStack(object):

    def __init__(self):
        self.top_idx = -1
        self.size = 1000
        self.arr = [0] * self.size

    def push(self, x):
        if self.top_idx < self.size - 1:
            self.top_idx += 1
            self.arr[self.top_idx] = x

    def pop(self):
        if self.top_idx == -1:
            return -1
        x = self.arr[self.top_idx]
        self.top_idx -= 1
        return x

    def top(self):
        if self.top_idx == -1:
            return -1
        return self.arr[self.top_idx]

    def empty(self):
        return self.top_idx == -1

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()