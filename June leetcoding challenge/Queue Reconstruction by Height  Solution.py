  
from functools import cmp_to_key

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key=cmp_to_key(lambda x, y: self.compare(x,y)))
        new_list = []
        
        for p in people:
            new_list.insert(p[1], p)
        
        return new_list
        
    def compare(self, a, b):
        if (a[0] == b[0]):
            return a[1] - b[1]
        else:
            return b[0] - a[0]
