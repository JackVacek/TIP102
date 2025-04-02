'''
You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. 
The tree has the following form:

Leaf nodes have an integer value.
Non-leaf nodes have a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated as follows:

If the node is a leaf node, the yield is the value of the node.
Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
Return the result of evaluating the root node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. 
Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    if not root.left and not root.right:
        return root.val
    l=calculate_yield(root.left)
    r=calculate_yield(root.right)
    if root.val=='+':
        return l + r
    if root.val=='-':
        return l - r
    if root.val=='*':
        return l * r
    if root.val=="/":
        return l/r
root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))