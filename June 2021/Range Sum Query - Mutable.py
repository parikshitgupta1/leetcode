class NumArray:
    class Node:
        def __init__(self, lx, rx):
            self.lx = lx
            self.rx = rx
            self.left = None
            self.right = None
            self.sum = 0

    def __buildTree(self, arr: List[int], i: int, j: int) -> Node:
        if i == j:  # Leaf node condition
            root = self.Node(i, j)
            root.sum = arr[i]
        else:  # Interval nodes
            root = self.Node(i, j)
            mid = i + (j - i) // 2
            root.left = self.__buildTree(arr, i, mid)
            root.right = self.__buildTree(arr, mid+1, j)
            root.sum = root.left.sum + root.right.sum
        return root

    def __updateTree(self, root: Node, index: int, value: int) -> Node:
        if root.lx == index and root.rx == index:
            root.sum = value
        else:
            mid = root.lx + (root.rx - root.lx) // 2
            if index <= mid:
                root.left = self.__updateTree(root.left, index, value)
            else:
                root.right = self.__updateTree(root.right, index, value)
            root.sum = root.left.sum + root.right.sum
        return root

    def __checkOverlap(self, nodeInterval: Tuple[int],
                       queryInterval: Tuple[int]) -> int:
        ix, iy = nodeInterval
        jx, jy = queryInterval

        if ix >= jx and iy <= jy:  # Complete overlap
            return 0
        elif iy < jx or ix > jy:  # No overlap
            return 1
        else:  # Partial overlap
            return 2

    def __sumRange(self, root: Node, i: int, j: int) -> int:
        k = self.__checkOverlap((root.lx, root.rx), (i, j))
        if k == 0:
            return root.sum
        elif k == 1:
            return 0
        else:
            return self.__sumRange(root.left, i, j) + \
                self.__sumRange(root.right, i, j)

    def __init__(self, nums):
        self.root = self.__buildTree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        self.root = self.__updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.__sumRange(self.root, left, right)
