class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sum = 0
        for i in shift:
            if i[0] == 0:
                sum += i[1]
            else:
                sum -= i[1]
        sum = sum % len(s)
        return s[sum:]+s[:sum]
