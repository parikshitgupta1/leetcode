class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

    def addWord(self, word):
        current = self
        i = len(word) - 1
        while i >= 0:
            index = ord(word[i]) - 97
            if not current.children[index]:
                current.children[index] = Trie()
            current = current.children[index]
            i -= 1
        current.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stack = []
        self.words = Trie()
        for word in words:
            self.words.addWord(word)

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        current = self.words
        pop = len(self.stack) - 1
        while pop >= 0:    
            index = ord(self.stack[pop]) - 97
            if current.is_word:
                return True
            if not current.children[index]:
                return False
            current = current.children[index]
            pop -= 1
        return current.is_word
