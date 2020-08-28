class Solution:
    def rand10(self):
        
        c = (rand7() - 1)*7 + rand7() - 1
        return self.rand10() if c>=40 else (c%10) +1
