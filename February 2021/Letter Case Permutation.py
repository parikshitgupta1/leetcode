class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        letter_indexes = [i for i in range(len(S)) if not S[i].isdigit()]
        my_set = set()
        res = [S]
        for index in letter_indexes:
            for word in res:
                i = index
                for i in range(index, len(word)):
                    if not word[i].isdigit():
                        my_set.add(word[:i]+word[i].upper()+word[i+1:])
                        my_set.add(word[:i]+word[i].lower()+word[i+1:])
    
            res += list(my_set)
            res = list(set(res))
        return res
