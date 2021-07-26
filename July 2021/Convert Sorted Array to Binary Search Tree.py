from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def addNodeToBST(start_index: int, end_index: int) -> TreeNode:
            if start_index > end_index:
                return None  # Base case
            mid_index = (start_index + end_index + 1) // 2
            root = TreeNode(nums[mid_index])
            root.left = addNodeToBST(start_index, mid_index-1)  
            root.right = addNodeToBST(mid_index+1, end_index)  
            return root

        root = addNodeToBST(0, len(nums)-1)
        return root
