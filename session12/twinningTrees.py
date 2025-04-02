class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_identical(root1, root2):
    if not root2 and not root1:
        return True
    elif not root1 and root2:
        return False
    elif not root2 and root1:
        return False
    elif root1.val != root2.val:
        return False
    l=is_identical(root1.left,root2.left)
    r=is_identical(root1.right,root2.right)
    return root1.val == root2.val and l and r
    


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))
root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))