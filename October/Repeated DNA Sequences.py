from collections import Counter
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter(s[i:i+10] for i in range(len(s) - 9))

        return [x for x in cnt if cnt[x] > 1]
