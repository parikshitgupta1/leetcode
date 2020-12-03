class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        root_list = []
        
        queue = [root]
        
        while len(queue) > 0:
            root_list.append([queue[0].val,queue[0]])
            
            if queue[0].left:
                queue.append(queue[0].left)
            
            if queue[0].right:
                queue.append(queue[0].right)
            
            queue = queue[1:]
        
        root_list.sort()
        
        root = root_list[0][1]
        temp = root
        
        for x in root_list[1:]:
            temp.right = x[1]
            temp.left = None
            temp = temp.right
        temp.right = None
        temp.left = None
        return root
