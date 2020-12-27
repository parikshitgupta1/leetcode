class Solution:
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(arr)):
            graph[arr[i]].append(i)

        visited = set()
        src, dest = 0, len(arr) - 1
        queue = deque()
        queue.append((src, 0))
        visited.add(src)
        while queue:
            node, dist = queue.popleft()
            if node == dest:
                return dist
            for child in [node - 1, node + 1] + graph[arr[node]][::-1]:
                if 0 <= child < len(arr) and child != node and child not in visited:
                    visited.add(child)
                    if child == dest:
                        return dist + 1
                    queue.append((child, dist + 1))
        return -1
