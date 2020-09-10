from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        A = 0
        d = Counter(secret) & Counter(guess)
        B = sum(d.values())
        
        for x, y in zip(secret,guess):
            if x == y:
                A += 1
             
                
        return f"{A}A{B-A}B"
