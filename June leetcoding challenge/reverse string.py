class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # First method to solve this is use the inbuilt reverse function
           # s.reverse()
            
        # Second method is to use Two Pointer or Sliding Window technique
        i = len(s) -1
        j = 0
        while i>=j:
            s[j],s[i] = s[i],s[j]
            i = i-1
            j =j+1
        return s
