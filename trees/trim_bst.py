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

def trimBST(root, low, high):
    if root.val == low:
        root = root.right
    else:
        prev = root
        if low > root.val:
            curr = root.right
            root = root.right
        else:
            curr = root.left
        while curr.val != low:
            prev = curr
            if low > curr.val:
                curr = curr.right
            else:
                curr = curr.left
            print(curr.val)
        if prev.right and prev.right.val == curr.val:
            if curr.right:
                prev.right = curr.right
            else:
                prev.right = None
        else:
            if curr.right:
                prev.left = curr.right
            else:
                prev.left = None

    if root.val == high:
        root.right = None
    else:
        prev = root
        if high > root.val:
            curr = root.right
            root = root.right
        else:
            curr = root.left
        while curr.val != high:
            prev = curr
            if high > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        print(curr.val, prev.val)
        if prev.right and prev.right.val == curr.val:
            if curr.left:
                prev.right = curr.left
            else:
                prev.right = None
        else:
            root = curr.left
    return root

test = TreeNode(val=3, left=TreeNode(val=0, left=None, right=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=None)),
                 right=TreeNode(val=4, left=None, right=None))
test2 = TreeNode(val=6, left=TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1, left=None, right=None),
                right=TreeNode(val=3, left=None, right=None)), right=TreeNode(val=5, left=None, right=None)), right=None)

printTree(test)
print('')
printTree(test2)
print('')
printTree(trimBST(test, 0, 4))
# printTree(trimBST(test2, 1, 4))
