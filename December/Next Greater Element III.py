class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = [int(i) for i in str(n)]
        for i in range(2, len(n) + 1):
            b, f = 1, n[-i]
            for j in range(1, 10 - f):
                if f + j in n[-i + 1:]:
                    b = 0
                    break
            if b == 1: continue
            n[n.index(f + j, -i)], n[-i] = f, f + j
            n[-i + 1:] = sorted(n[-i + 1:])
            n = int("".join([str(i) for i in n]))
            return n if n < 2 ** 31 else -1
        return -1
