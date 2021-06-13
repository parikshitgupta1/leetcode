class Solution:
    def is_palin(self, s):
      if not s: 
        return True 
      left, right = 0, len(s) - 1
      while left <= right: 
        if s[left] != s[right]: 
          return False
        left += 1 
        right -= 1
      return True 

    def palindromePairs(self, words):
        # Write your code here
        value_to_index = {
          v : i for i, v in enumerate(words)
        }

        result_set = set()
        for i, word in enumerate(words): 
          n = len(word)
          for k in range(n + 1): 
            left_part = word[:k]
            if self.is_palin(word[k : n]) and left_part[::-1] in value_to_index: 
              if value_to_index[left_part[::-1]] == i: 
                continue 
              result_set.add((i, value_to_index[left_part[::-1]]))
          
          for k in range(n, -1, -1): 
            right_part = word[k : n]
            if self.is_palin(word[0 : k]) and right_part[::-1] in value_to_index: 
              if value_to_index[right_part[::-1]] == i: 
                continue 
              result_set.add((value_to_index[right_part[::-1]], i))
        
        return [[a, b] for a, b in result_set]
