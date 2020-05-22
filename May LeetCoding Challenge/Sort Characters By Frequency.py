from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        res = ""
        for k,v in freq.most_common():
            ans = ""
            for i in range(v):
                ans += k
            res += ans
        return res
