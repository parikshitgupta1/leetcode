class Solution:
    def isPalindrome(self, s: str) -> bool:
        string2 = ""
        for character in s.lower():
            if character.isalnum():
                string2 += character
        if string2 == string2[::-1]:
            return True
        return False
