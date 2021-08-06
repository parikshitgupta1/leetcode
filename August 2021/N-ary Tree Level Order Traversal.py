from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children 

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return list()

        queue = [[root]] 
        result = list()

        while queue:
            level_nodes = queue.pop(0)  
            level_vals = list()
            children = list()
            for node in level_nodes:
                level_vals.append(node.val)
                if node.children:
                    children += node.children  
            if children:
                queue.append(children)
            result.append(level_vals)

        return result
