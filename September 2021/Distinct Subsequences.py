class Solution:
    def numDistinct(self, S, T):
        # write your code here
        n = len(S)
        m = len(T)
        
        f = [0] * (m+1)
        f[0] = 1

        for i in range(n):
            for j in range(m, 0, -1):
                if T[j-1] == S[i]:
                    f[j] += f[j-1]
        

        return f[-1]
