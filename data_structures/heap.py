class Heap():
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
        curr_idx = len(self.list) - 1
        while curr_idx != 0:
            curr = self.list[curr_idx]
            parent_idx = (curr_idx - 1) // 2
            parent = self.list[parent_idx]
            if curr >= parent:
                return
            self.list[curr_idx] = parent
            self.list[parent_idx] = curr
            curr_idx = parent_idx

    def pop(self):
        head = self.list[0]
        self.list[0] = self.list.pop()
        curr_idx = 0
        while curr_idx < len(self.list) - 1:
            l_child_idx = (curr_idx * 2) + 1
            r_child_idx = (curr_idx * 2) + 2
            smallest_idx = curr_idx
            if l_child_idx < len(self.list) and self.list[l_child_idx] < self.list[smallest_idx]:
                smallest_idx = l_child_idx
            if r_child_idx < len(self.list) and self.list[r_child_idx] < self.list[smallest_idx]:
                smallest_idx = r_child_idx
            if smallest_idx != curr_idx:
                tmp = self.list[curr_idx]
                self.list[curr_idx] = self.list[smallest_idx]
                self.list[smallest_idx] = tmp
                curr_idx = smallest_idx
        return head

    def top(self):
        return self.list[0]


test = Heap()
l = [10, 3, 8, 9, 4]
for i in l:
    test.push(i)
print(test.list)
# print(test.pop())
# print(test.list)
