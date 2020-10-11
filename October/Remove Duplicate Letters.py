class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={}
        used=set()
        stack=deque()
        n=len(s)
        for char in s:
            d[char]=1 if char not in d else d[char]+1
        for char in s:
            d[char]-=1
            if char not in used:
                while stack and d[stack[-1]]>0 and stack[-1]>char:
                    used.remove(stack.pop())
                stack.append(char)
                used.add(char)

        ans =''
        for char in stack:
            ans+=char
        return (ans)
