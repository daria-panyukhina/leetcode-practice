class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dict = dict()
        self.last_node = None
        self.first_node = None

    def get(self, key):
        if key not in self.dict:    # if not in dict -> -1
            return -1
        self.promote(self.dict[key])
        return self.dict[key].val

    def put(self, key, value):
        if key in self.dict:
            self.promote(self.dict[key])
            self.dict[key].val = value
            return
        new_node = Node(key, value)
        self.dict[key] = new_node
        self.size += 1
        self.push_back(new_node)

    def push_back(self, node):
        if self.last_node:  # add to tne end of LL
            self.last_node.next = node
            node.prev = self.last_node
            self.last_node = node
            self.evict()
            return
        self.first_node = node
        self.last_node = node

    def promote(self, node):
        if node == self.last_node:
            return
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node.next.prev = None
            self.first_node = node.next
        self.push_back(node)

    def evict(self):
        if self.size > self.capacity:  # check the capacity, if too much -> evict the first
            sec_node = self.first_node.next
            del self.dict[self.first_node.key]
            self.first_node = sec_node
            self.first_node.prev = None
            self.size -= 1


obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
obj.put(1, 1)
obj.put(4, 1)
print(obj.get(2))
