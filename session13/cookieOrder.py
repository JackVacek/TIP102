from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

        
def build_cookie_tree(descriptions):
    d = {}
    root = None
    for parent, child, isLeft in descriptions:
        if parent not in d:
            d[parent] = TreeNode(parent)
        if not root:
            root = d[parent]
        if child not in d:
            d[child] = TreeNode(child)
        if isLeft:
            d[parent].left = d[child]
        else:
            d[parent].right = d[child]
                                
    return root

descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

descriptions3 = [
    ["Ginger Snap", "Snickerdoodle", 0],
]
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
print_tree(build_cookie_tree(descriptions3))


'''
{
    chocolate chip => TreeNode(chocolate chip)
}
currentNode = Chocolate chip

            Chocolate chip
             /          \
            /            \
        peanut butter   oatmeal
        
'''