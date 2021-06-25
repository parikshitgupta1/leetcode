class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n+1)]

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for i, j in edges:
            if uf.find(i) == uf.find(j):
                return [i, j]
            else:
                uf.union(i, j)
        return None
