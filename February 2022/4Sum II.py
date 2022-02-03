class Solution:
    def fourSumCount(self, A, B, C, D):
        res = {}
        for i in A:
            for j in B:
                sum_ = i + j
                if sum_ not in res:
                    res[sum_] = 1
                else:
                    res[sum_] += 1
        count = 0
        for i in C:
            for j in D:
                if 0 - j - i in res:
                    print(res[0 - i - j])
                    count += res[0 - i - j]
        return count
