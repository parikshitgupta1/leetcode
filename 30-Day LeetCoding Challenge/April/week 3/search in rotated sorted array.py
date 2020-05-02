class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        
        head = 0
        tail =len(nums)-1
        indices = [i for i in range(len(nums))]
        offset=0
        if nums[head]>nums[tail]:   
            while tail>head+1:
                middle=int((head+tail)/2)
                
                if nums[middle]>=nums[head]:
                    head=middle
                else:
                    tail = middle
            #nums = nums[tail:len(nums)]+nums[0:tail]
            #indices = indices[tail:len(nums)]+indices[0:tail]

        
            offset = tail    
        
        
        head = 0
        tail = len(nums)-1
        while tail>head+1:
            middle = int((head+tail)/2)
            if nums[(offset+middle)%len(nums)]>=target:
                tail=middle
            else:
                head = middle

        if nums[(offset+tail)%len(nums)]==target:
            return indices[(offset+tail)%len(nums)]
        elif nums[(offset+head)%len(nums)]==target:
            return indices[(offset+head)%len(nums)]            
        else:
            return -1
