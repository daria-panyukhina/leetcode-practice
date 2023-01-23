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

def binaryTreePaths(root):
    if not root:
        return
    res = []
    stack = [root]
    visited_set = set()
    while stack:
        curr = stack[len(stack)-1]
        if not curr.left and not curr.right:
            visited_set.add(curr)
            res.append('->'.join(str(i.val) for i in stack))
            stack.pop()
        else:
            if curr.left and (curr.left not in visited_set):
                stack.append(curr.left)
            elif curr.right and (curr.right not in visited_set):
                stack.append(curr.right)
            else:
                visited_set.add(curr)
                stack.pop()
    return res




test = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
test1 = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None))
test2 = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
test3 = TreeNode(val=3, left=TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None)),
                 right=TreeNode(val=4, left=None, right=None))
printTree(test3)
print('')
print(binaryTreePaths(test3))
t = [test3, test, test1]
