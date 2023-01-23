class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):

        return self.list.pop()

    def is_empty(self):
        return len(self.list) == 0

    def top(self):
        if self.is_empty():
            return
        return self.list[-1]


class QueueWithMin:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def move_stack(self):
        if self.stack1.is_empty():
            return
        new_item = self.stack1.pop()
        new_item[1] = new_item[0]
        self.stack2.push(new_item)
        while not self.stack1.is_empty():
            new_item = self.stack1.pop()
            prev_item = self.stack2.top()
            if new_item[0] > prev_item[1]:
                new_item[1] = prev_item[1]
            self.stack2.push(new_item)

    def enqueue(self, item):
        new_item = [item, item]
        if self.stack1.top():
            if self.stack1.top()[1] < new_item[1]:
                new_item[1] = self.stack1.top()[1]
        self.stack1.push(new_item)

    def dequeue(self):
        try:
            if self.stack2.is_empty():
                self.move_stack()
            return self.stack2.pop()[0]
        except IndexError:
            return 'End of the queue'

    def peek_min(self):
        if self.stack2.is_empty():
            self.move_stack()
        if not self.stack1.is_empty():
            if self.stack1.top()[1] < self.stack2.top()[1]:
                return self.stack1.top()[1]
        return 'min', self.stack2.top()[1]


test = QueueWithMin()
list1 = [1, 5, 2]
list2 = [3, 1, 6]
for i in list1:
    test.enqueue(i)
print(test.dequeue())
print(test.peek_min())
for i in list2:
    test.enqueue(i)
print(test.dequeue())
print(test.dequeue())
for i in range(3):
    print(test.peek_min())
    print(test.dequeue())
print(test.dequeue())
print(test.dequeue())