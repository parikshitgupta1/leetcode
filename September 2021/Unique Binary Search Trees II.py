class Solution:
    def generateTrees(self, n):
        results = self.build_tree(1, n)
        return results
    
    def build_tree(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        
        results = []
        for i in range(start, end + 1):
            left_results = self.build_tree(start, i - 1)
            right_results = self.build_tree(i + 1, end)
            for left in left_results:
                for right in right_results:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    results.append(root)
        return results
