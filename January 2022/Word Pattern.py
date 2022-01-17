class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
	#splitting the string to keep track of each word
        words = str.split(" ")

	#If number of words does not match the letters of the pattern then we return false
        if len(words) != len(pattern):
            return False

   
	#Dictionary to keep track of pattern and the words
        d = dict()

        for i in range(len(pattern)):
            current_char = pattern[i]
       	    #if there is no word associated with the pattern character
            if not d.get(current_char):
        	# Check if word is not present for another pattern character
                if words[i] in d.values():
                    return False
            	#associate the word with the pattern character
                d[current_char] = words[i]
            else:
            	#if word is already associated for the pattern character, check if the word is same as the word in the sequence
                if d.get(current_char) != words[i]:
                    return False

        return True
