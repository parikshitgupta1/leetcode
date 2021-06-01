from collections import Counter

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        sets = Counter()
        for w in words:
            key = frozenset(w)
            sets[key] = max(sets[key], len(w))

        max_len = 0
        for x, vx in sets.items():
            for y, vy in sets.items():
                if not x.intersection(y):
                    max_len = max(max_len, vx * vy)
        return max_len
