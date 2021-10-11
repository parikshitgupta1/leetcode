from typing import List

class Solution:
    class TrieNode:
        def __init__(self, c='/'):
            self.c = c
            self.word = ''
            self.children = [None for _ in range(26)]
        
        
    def buildTrie(self, words):
        root = self.TrieNode()
        for word in words:
            node = root
            for c in word:
                if not node.children[ord(c)-ord('a')]:
                    node.children[ord(c)-ord('a')] = self.TrieNode(c)
                node = node.children[ord(c)-ord('a')]
            node.word = word
        return root
    
    
    def inbounds(self, board, r, c):
        return r >= 0 and r < len(board) and c >= 0 and c < len(board[0])
    
        
    def dfs(self, root, board, r, c, ans):
        if root.word:
            ans.add(root.word)
        board[r][c] = '.'
        if self.inbounds(board, r+1, c) and board[r+1][c] != '.' and root.children[ord(board[r+1][c])-ord('a')]:
            self.dfs(root.children[ord(board[r+1][c])-ord('a')], board, r+1, c, ans)
        if self.inbounds(board, r-1, c) and board[r-1][c] != '.' and root.children[ord(board[r-1][c])-ord('a')]:
            self.dfs(root.children[ord(board[r-1][c])-ord('a')], board, r-1, c, ans)
        if self.inbounds(board, r, c+1) and board[r][c+1] != '.' and root.children[ord(board[r][c+1])-ord('a')]:
            self.dfs(root.children[ord(board[r][c+1])-ord('a')], board, r, c+1, ans)
        if self.inbounds(board, r, c-1) and board[r][c-1] != '.' and root.children[ord(board[r][c-1])-ord('a')]:
            self.dfs(root.children[ord(board[r][c-1])-ord('a')], board, r, c-1, ans)
        board[r][c] = root.c
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        root = self.buildTrie(words)
        ans = set()
        for r in range(n):
            for c in range(m):
                if root.children[ord(board[r][c])-ord('a')]:
                    self.dfs(root.children[ord(board[r][c])-ord('a')], board, r, c, ans)
        return list(ans)
