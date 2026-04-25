class St:
    def __init__(self):
        self.stack = []

    # push element
    def push(self, data):
        self.stack.append(data)

    # pop element
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop()

    # peek top element
    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

    # display stack
    def display(self):
        print(self.stack)


s = St()

s.push(10)
s.push(20)
s.push(30)

s.display()       # [10, 20, 30]
print(s.pop())    # 30
print(s.peek())   # 20
s.display()       # [10, 20]
    




