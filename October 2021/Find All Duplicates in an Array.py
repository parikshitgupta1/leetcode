class Solution(object):
    def findDuplicates(self, nums):
        dup = []
        unik = {}
        for x in nums:
            if x not in unik:
                unik[x] = 1
            else:
                    dup.append(x)
                    unik[x] += 1
        return dup
