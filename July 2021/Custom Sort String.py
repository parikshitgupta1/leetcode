from collections import Counter


class Solution:
    def customSortString(self, order: str, string: str) -> str:
        ch_count = Counter(string)
        result = str()
        for ch in order:
            try:
                result += ch * ch_count.pop(ch)
            except KeyError:
                continue
        while ch_count:
            ch, count = ch_count.popitem()
            result += ch * count

        return result
