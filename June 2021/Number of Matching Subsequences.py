class Solution:

    def __isSubSequence(self, string1, string2, m, n):
        # Base Cases
        if m == 0:
            return True
        if n == 0:
            return False

        # If last characters of two strings are matching
        if string1[m-1] == string2[n-1]:
            return self.__isSubSequence(string1, string2, m-1, n-1)
        # If last characters are not matching
        return self.__isSubSequence(string1, string2, m, n-1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        n = len(s)
        word_count = {word: words.count(word) for word in set(words)}
        for word, count in word_count.items():
            if self.__isSubSequence(word, s, len(word), n):
                ans += count
        return ans
