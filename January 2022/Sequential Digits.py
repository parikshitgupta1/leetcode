from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        i = 0
        j = len(str(low))
        num = 0
        result = [] 
        digits = "1234567890"
        length = len(digits)
        while num < high:
            num = int(digits[i:i+j])
            if num in range(low, high+1):
                result.append(num)
            i += 1
            if i + j >= length:
                j += 1
                i = 0
        return result
