class Solution:
    def findIntegers(self, n: int) -> int:
        upper_bin = bin(n+1)[2:]
        length = len(upper_bin)

        dp = [1, 2] + [0]*(length-2)
        for i in range(2, length):
            dp[i] = dp[i-1] + dp[i-2]

        flag = False  
        ans = 0
        for i in range(length):
            if upper_bin[i] == '0':
                continue
            if flag:
                break
            if i > 0 and upper_bin[i-1] == '1':
                flag = True
            ans += dp[-i-1]

        return ans
