def most_popular_cookie_combo(root):
    d = {}
    def total(node):
        if not node:
            return 0
        l_sum = total(node.left)
        r_sum = total(node.right)
        totall = node.val + l_sum + r_sum
        d[totall] = d.get(totall,0)+1
        return totall
    total(root)
    maxFreq=max(d.values())
    res = [i for i,c in d.items() if c == maxFreq]
    return res
