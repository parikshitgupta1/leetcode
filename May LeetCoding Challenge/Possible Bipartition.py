import collections


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0): # coloring
            if node in color:
                return color[node] == c # if we ever color a red node blue (or a blue node red), then we've reached a conflict.
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node]) # includes bitwise XOR operator

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)





N = 4
dislikes = [[1, 2], [1, 3], [2, 4]]

foo = Solution()
print(foo.possibleBipartition(N, dislikes))
