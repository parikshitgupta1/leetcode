class Solution:

    def orderlyQueue(self, S, K):
        
        if K > 1:
            lst = list(S)
            lst.sort()
            return ''.join(lst)
        min_char = min(set(S))
        ans = S
        for i in range(len(S)):
            if S[i] == min_char:
                ans = min(ans, S[i:] + S[:i])
        return ans
