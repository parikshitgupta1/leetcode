from typing import List


class Solution:
    def is_subsequence(self, word1, word2):
        n = len(word1)
        index = 0  
        for ch in word2:
            if index < n and ch == word1[index]:
                index += 1
        return index == n 

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)  
        for s in strs:
            res = [self.is_subsequence(s, t) for t in strs]
            if sum(res) == 1:
                return len(s)  
        return -1
