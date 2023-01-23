from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        path1 = deque()
        path2 = deque()
        self.find_path(path1, root, p)
        self.find_path(path2, root, q)
        i = 0
        n = min(len(path1), len(path2))
        while i < n and path1[i] == path2[i]:
            i += 1
        return path1[i - 1]

    def find_path(self, deque, curr_node, x):
        if not curr_node:
            return False
        if curr_node == x:
            deque.appendleft(curr_node)
            return True
        if self.find_path(deque, curr_node.left, x):
            deque.appendleft(curr_node)
            return True
        if self.find_path(deque, curr_node.right, x):
            deque.appendleft(curr_node)
            return True
        return False


s = Solution()
test = TreeNode(val=3, left=None, right=None)
test.left = TreeNode(val=5, left=TreeNode(val=6, left=None, right=None), right=TreeNode(val=2, left=None, right=None))
test.left.right = TreeNode(val=2, left=TreeNode(val=7, left=None, right=None),
                           right=TreeNode(val=4, left=None, right=None))
test.right = TreeNode(val=1, left=TreeNode(val=0, left=None, right=None), right=TreeNode(val=8, left=None, right=None))

x = test.left
y = test.left.right.right
print(x, y)
print(s.lowestCommonAncestor(test, x, y))
# print(s.find_path(d, test, x))
