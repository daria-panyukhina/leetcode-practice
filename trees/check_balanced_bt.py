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


def maxDepth(node):
    if not node:
        return 0
    return max(maxDepth(node.left), maxDepth(node.right)) + 1


def isBalanced2(root):
    if not root:
        return 0
    h1 = isBalanced2(root.left)
    h2 = isBalanced2(root.right)
    if h1 > -1 and h2 > -1 and abs(h1 - h2) <= 1:
        return max(h1, h2) + 1
    else:
        return -1


def isBalanced(root):
    return isBalanced2(root) != -1


test = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None),
                right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None),
                               right=TreeNode(val=7, left=None, right=None)))

test2 = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=TreeNode(val=3, left=None, right=None)))


# print(isBalanced(test4))
# print(maxDepth2(test2))
# print(treeHeight(test2, 1))
print(isBalanced(test))
print(isBalanced(test))
