from typing import List


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        def helper( char, table ):
            
            if char not in table:
                table[char] = {}
            

            return table[char]
        
        # -----------------------
        
        # update new word into trie
        table = self.trie
        for char in word:
            table = helper( char, table)
        
        # use '@' as ending symbol
        table['@'] = {}
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        def helper( char, table):
            
            if char in table:
                return table[char]
            else:
                return None
            
        # -----------------------
        
        # search word in trie
        table = self.trie
        
        for char in word:
            table = helper( char, table)
            
            if table is None:
                return False
        
        # use ending symbol to judge whether current word exist in our trie or not
        return ( '@' in table )
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        def helper( char, table):
            
            if char in table:
                return table[char]
            else:
                return None
            
        # -----------------------
        
        # check the prefix exist in trie or not
        table = self.trie
        
        for char in prefix:
            table = helper( char, table)
            
            if table is None:
                return False
        
        return True
