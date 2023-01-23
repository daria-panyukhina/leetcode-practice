class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxHeight(node, h):
    h1 = 0
    h2 = 0
    if not node.left and not node.right:
        return h
    if node.left:
        h1 = maxHeight(node.left, h+1)
    if node.right:
        h2 = maxHeight(node.right, h+1)
    return max(h1, h2)

def minHeight(node, h):
    h1 = 0
    h2 = 0
    if not node.left and not node.right:
        return h
    if node.left:
        h1 = minHeight(node.left, h + 1)
    if node.right:
        h2 = minHeight(node.right, h + 1)
    if h1 == 0:
        return h2
    if h2 == 0:
        return h1
    return min(h1, h2)

def maxDepth(root):
    if not root:
        return
    else:
        return maxHeight(root, 1)

test = TreeNode(val=3, left=TreeNode(val=9, left=None, right=None),
                right=TreeNode(val=20, left=TreeNode(val=15, left=None, right=None),
                               right=TreeNode(val=7, left=None, right=None)))

test2 = TreeNode(val=3, left=None,
                right=None)

# print(maxHeight(test2, 1))
print(maxDepth(test))