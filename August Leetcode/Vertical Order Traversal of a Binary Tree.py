from collections import defaultdict

class Solution:

    # solution 1   
    def __init__(self):
        self.min = float('inf')
        self.max = -float('inf')
        self.d = defaultdict(list)
        
    def dfs(self, root, x, y):
        self.min = min(self.min, x)
        self.max = max(self.max, x)
        
        self.d[x].append((y, root.val))
        
        if (root.left):
            self.dfs(root.left, x-1, y+1)
        if (root.right):
            self.dfs(root.right, x+1, y+1)
        
    def verticalTraversal(self, root):
        res = []
        if root == None:
            return res
        
        self.dfs(root, 0, 0)
        
        for i in range(self.min, self.max+1):
            
            tmp = []
            
            for _,k in sorted(self.d[i]):
                tmp.append(k)
            if tmp :
                res.append(tmp)
                
        return res
