class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        ans = []
        num1 = None
        count1 = 0
        num2 = None
        count2 = 0
        for i in nums:
            if num1 == i:
                count1 += 1
            elif num2 == i:
                count2 += 1
            elif count1 == 0:
                num1 = i
                count1 += 1
            elif count2 == 0:
                num2 = i
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        if nums.count(num1) > len(nums) // 3:
            ans.append(num1)
        if nums.count(num2) > len(nums) // 3:
            ans.append(num2)
            
            
        return ans
