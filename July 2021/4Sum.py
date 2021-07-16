from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = list()

        if n < 4:
            return ans
        pair_sums = dict()
        for i in range(0, n-1):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                if s in pair_sums:
                    pair_sums[s].append((i, j))
                else:
                    pair_sums[s] = [(i, j)]

        for s, pairs1 in pair_sums.items():  
            req = target - s
            if req in pair_sums:
                pairs2 = pair_sums[req] 

                for i, j in pairs1:  
                    for k, l in pairs2:  

                        if len(set([i, j, k, l])) == 4:
                            temp = sorted([nums[i], nums[j], nums[k], nums[l]])

                            if temp not in ans:
                                ans.append(temp)

        return ans
