from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        ans = [0] * n
        count = [1] * n  

        def counter(node, parent):
            for child in tree[node]:
                if child != parent:
                    counter(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]  
        counter(0, -1)

        def add_rest(node, parent):
            for child in tree[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (n-count[child])
                    add_rest(child, node)
        add_rest(0, -1)
        return ans
