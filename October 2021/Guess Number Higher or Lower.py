class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n+1
        while start < end:
            mid = int((start+end)/2)
            if guess(mid) == -1:
                end = mid
            elif guess(mid) == 1:
                start = mid + 1
            elif guess(mid) == 0:
                return mid
        return -1
