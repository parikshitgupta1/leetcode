
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def isAnagram(s, t):
            def frequencies(s):
                f = dict()
                for c in s:
                    if c not in f:
                        f[c] = 0
                    f[c] += 1
                return f
            return frequencies(s) == frequencies(t)
        powers_of_two = [2**i for i in range(31)] # log2(10^9) == 29.89
        return any(isAnagram(str(N), str(p)) for p in powers_of_two)
