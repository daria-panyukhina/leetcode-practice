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


#  Solution 1

def findLeftSucc(node):
    if not node:
        return
    if not node.right:
        return node.val
    return findLeftSucc(node.right)


def findRightSucc(node):
    if not node:
        return
    if not node.left:
        return node.val
    return findRightSucc(node.left)


def isValidBST(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    if not root.left:
        if isValidBST(root.right):
            right_successor = findRightSucc(root.right)
            return right_successor > root.val
    if not root.right:
        if isValidBST(root.left):
            left_successor = findLeftSucc(root.left)
            return left_successor < root.val
    if root.left and root.right:
        if isValidBST(root.left) and isValidBST(root.right):
            left_successor = findLeftSucc(root.left)
            right_successor = findRightSucc(root.right)
            return left_successor < root.val < right_successor
    return False


# Solution 2

def valid(node, low, high):
    if not node:
        return True
    check1 = valid(node.left, low, node.val)
    check2 = valid(node.right, node.val, high)
    return check1 and check2 and node.val > low and node.val < high

def isValidBST_2(root):
    return valid(root, float('-inf'), float('inf'))


test = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=None))

test2 = TreeNode(val=5, left=TreeNode(val=4, left=None, right=None),
                 right=TreeNode(val=6, left=TreeNode(val=3, left=None, right=None),
                                right=TreeNode(val=7, left=None, right=None)))

print(isValidBST(test2))
print(valid(test2, float('-inf'), float('inf')))

