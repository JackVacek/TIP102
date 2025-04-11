def count_cookie_paths(root, target_sum):
    def dfs(node, currentSum):
        if not node:
            return 0
        currentSum += node.val
        if not node.left and not node.right:
            return 1 if currentSum == target_sum else 0
        return dfs(node.left, currentSum) + dfs(node.right, currentSum)
    return dfs(root, 0)