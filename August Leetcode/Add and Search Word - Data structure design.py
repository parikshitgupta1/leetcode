class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. less space than 93%
        """
        n = len(word)
        for s in self.dict:
            if len(s) != n:
                continue
            
            flag = True
            for i in range(len(word)):
                if word[i]=='.':
                    continue
                
                if word[i]!=s[i]:
                    flag = False
                    break
                    
            if flag:
                return True
        return False
