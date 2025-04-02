class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_old_growth(root, threshold):
    l,r=0,0
    curr=0
    if root.left:
        l=count_old_growth(root.left,threshold)
    if root.right:
        r=count_old_growth(root.right,threshold)
    if root.val > threshold:
        curr=1
    return curr + l + r

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))

print(count_old_growth(forest, 1000))