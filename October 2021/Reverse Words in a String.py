class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split(' ')[::-1]
        new_string = ""
        for i in range(0,len(list1)):
            if(list1[i]!=""):
                if(len(new_string)>0):
                    new_string+=" "
                new_string+=list1[i]
        return new_string
