class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, root, i, lst, inf, sup):
        if i < len(lst) and root.val > lst[i] > inf:
            root.left = TreeNode(lst[i])
            i = self.buildTree(root.left, i + 1, lst, inf, root.val)
        if i < len(lst) and root.val < lst[i] < sup:
            root.right = TreeNode(lst[i])
            i = self.buildTree(root.right, i + 1, lst, root.val, sup)
        return i

    def bstFromPreorder(self, preorder):
        inf = 1001
        root = TreeNode(preorder[0])
        self.buildTree(root, 1, preorder, -inf, inf)
        return root

def printTree(node):
    if not node:
        return
    print(node.val, end=' ')
    printTree(node.left)
    printTree(node.right)
    
test = [8, 5, 1, 7, 10, 12]
s = Solution()
printTree(s.bstFromPreorder(test))
