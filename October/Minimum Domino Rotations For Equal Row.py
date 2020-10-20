class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        min_value = float("inf")
        for idx in range(2):
            total =  min(self.traversal(A,B),self.traversal(B,A))
            if idx==1:
                total+=1
            if total<=len(A):
                min_value = min(min_value,total)
            A[0],B[0]=B[0],A[0]
        if min_value>len(A):
            return -1
        return min_value
    
    def traversal(self,A,B):
        top = A[0]
        count = 0
        for idx in range(1, len(A)):
            if top!=A[idx]:
                if top==B[idx]:
                    count+=1
                else:
                    return len(A)+1         
        return count
