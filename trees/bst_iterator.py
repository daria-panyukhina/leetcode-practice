class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root):
        self.stack = [root]
        self.visited_set = set()

    def next(self):
        while self.stack:
            curr = self.stack.pop()
            if curr.left and curr.left not in self.visited_set:
                self.stack.append(curr)
                self.stack.append(curr.left)
            else:
                self.visited_set.add(curr)
                if curr.right:
                    self.stack.append(curr.right)
                return curr.val
        else:
            raise StopIteration

    def hasNext(self):
        return not not self.stack

# def inorderTraversal2(root):
#     if not root:
#         return
#     stack = [root]
#     res = []
#     visited_set = set()
#     while stack:
#         curr = stack.pop()
#         if curr.left and curr.left not in visited_set:
#             stack.append(curr)
#             stack.append(curr.left)
#         else:
#             res.append(curr.val)
#             visited_set.add(curr)
#             if curr.right:
#                 stack.append(curr.right)
#     return res

# Your BSTIterator object will be instantiated and called as such:
test = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
obj = BSTIterator(test)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
# param_1 = obj.next()
# param_2 = obj.hasNext()

