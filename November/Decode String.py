class Solution:
    def decodeString(self, s: str) -> str:
        "abc3[cd]xyz"
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                temp = ""
                while (stack[-1] != "["):
                    temp += stack.pop()
                stack.pop()
                n = ""
                while (stack and stack[-1].isdigit()):
                    n += stack.pop()
                decoded = int(n[::-1]) * temp[::-1]
                for j in decoded:
                    stack.append(j)
        ans = "".join(ch for ch in stack)
        return ans
