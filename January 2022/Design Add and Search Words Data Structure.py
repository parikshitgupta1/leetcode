class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def __repr__(self):
        return repr(self.trie)
    
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for letter in word: 
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = True  # denotes a completed word
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchNode(self.trie, word)

    def searchNode(self, node, word: str) -> bool:
        for index, letter in enumerate(word):
            if letter == '.':
                return any(self.searchNode(node[w], word[index+1:]) for w in node if w != '*')
            if letter not in node: return False
            node = node[letter]
        return '*' in node
    
