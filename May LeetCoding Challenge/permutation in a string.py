class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = [0] * 26
        counter2 = [0] * 26
        for i in s1:
            counter1[ord(i) - 97] += 1
        n = len(s1)
        for j in range(len(s2)):
            if j >= n:
                counter2[ord(s2[j - n]) - 97] -= 1
            counter2[ord(s2[j]) - 97] += 1
            if counter1 == counter2:
                return True
        return False
                
