class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        length = len(words)
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i in range(length):
            if words[i][0].lower() in vowels:
                words[i] += 'ma'+ 'a' * (i + 1)
            else:
                words[i] = words[i][1:] + words[i][0] + 'ma'+ 'a' * (i + 1)
        return ' '.join(words)
