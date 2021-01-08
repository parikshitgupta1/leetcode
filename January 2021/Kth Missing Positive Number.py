class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        res = [i for i in range(0, 100000)]
        res2 = list(set(res).difference(arr))
        return (res2[k])
