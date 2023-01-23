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



def isSameTree(p, q):
    if not p and not q:
        return True
    if (not p and q) or (p and not q) or (p.val != q.val):
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)




test = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=None)
test1 = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=None))
test2 = TreeNode(val=1, left=TreeNode(val=2, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
test3 = TreeNode(val=5, left=TreeNode(val=4, left=None, right=None),
                 right=TreeNode(val=6, left=TreeNode(val=3, left=None, right=None),
                                right=TreeNode(val=7, left=None, right=None)))
# printTree(test)
print(isSameTree(test, test1))