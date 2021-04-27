class Solution:
    def isPowerOfThree(self, n) -> bool:
        while n % 3 == 0 and n >= 81:
            n = n / 81
        
        while n % 3 == 0 and n >= 3:
            n = n / 3
        
        if n == 1:
            return True

        return False


a = Solution()
print(a.isPowerOfThree(0))
