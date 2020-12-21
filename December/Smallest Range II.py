class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        n = len(A)
        ans = float("inf")
        for i in range(0, n - 1):
            cands = [A[0], A[i], A[i + 1] - 2 * K, A[-1] - 2 * K]
            ans = min(ans, max(cands) - min(cands))
        return min(ans, A[-1] - A[0])
