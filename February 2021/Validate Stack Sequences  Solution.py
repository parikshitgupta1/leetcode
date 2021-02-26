class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        popidx = 0
        for d in pushed:
            st.append(d)
            while st and st[-1] == popped[popidx]:
                st.pop()
                popidx += 1
        return not st
