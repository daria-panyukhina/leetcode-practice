class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def myTraversal(root, lst):
    if root.left:
        myTraversal(root.left, lst)
    lst.append(root.val)
    if root.right:
        myTraversal(root.right, lst)


def inorderTraversal(root):
    lst = []
    if not root:
        return
    myTraversal(root, lst)
    return lst


def inorderTraversal2(root):
    if not root:
        return
    stack = [root]
    res = []
    visited_set = set()
    while stack:
        curr = stack.pop()
        if curr.left and curr.left not in visited_set:
            stack.append(curr)
            stack.append(curr.left)
        else:
            res.append(curr.val)
            visited_set.add(curr)
            if curr.right:
                stack.append(curr.right)
    return res

def inorderTraversal3(root):
    if not root:
        return
    stack = [(root, False)]
    res = []
    while stack:
        curr = stack.pop()
        node = curr[0]
        visited = curr[1]
        if node.left and not visited:
            stack.append((node, True))
            stack.append((node.left, False))
        else:
            res.append(node.val)
            if node.right:
                stack.append((node.right, False))
    return res

def preorderTraversal(root):
    if not root:
        return
    stack = [root]
    res = []
    while stack:
        curr = stack.pop()
        # node = curr[0]
        # visited = curr[1]
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res

tree = TreeNode(val=1, left=None, right=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None), right=None))
tree2 = TreeNode(val=1, left=None, right=None)
print(inorderTraversal(tree))
print(inorderTraversal2(tree))
print(inorderTraversal3(tree))
print(preorderTraversal(tree))