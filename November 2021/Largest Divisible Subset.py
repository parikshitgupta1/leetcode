class Solution(object):
    def largestDivisibleSubset(self, nums):
        max_to_set = {-1 : set()}    
        nums.sort()

        for num in nums:

            num_set = set()         
            for max_in_s, s in max_to_set.items():
                if num % max_in_s == 0 and len(s) > len(num_set):
                    num_set = s

            max_to_set[num] = num_set | {num}    

        return list(max(max_to_set.values(), key = len))    
