class Solution:
    def hIndex(self, citations: List[int]) -> int:
        while citations and citations[0]<len(citations):
            citations.pop(0)
        return len(citations)
