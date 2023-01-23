from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(node):
    if not node:
        return
    print(node.val, end=' ')
    printTree(node.left)
    printTree(node.right)


def kthSmallest(root, k):
    if not root or k == 0:
        return
    stack = [root]
    visited_set = set()
    while stack and k > 0:
        curr = stack.pop()
        if curr.left and (curr.left not in visited_set):
            stack.append(curr)
            stack.append(curr.left)
        else:
            visited_set.add(curr)
            k -= 1
            if k == 0:
                return curr.val
            if curr.right:
                stack.append(curr.right)


test = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
test1 = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None))
test2 = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
test3 = TreeNode(val=3, left=TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None)),
                 right=TreeNode(val=4, left=None, right=None))
printTree(test3)
print('')
print(kthSmallest(test3, 3))
