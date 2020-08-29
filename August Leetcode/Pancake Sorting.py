class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def reverse(A,n):
            A[:n+1] = A[:n+1][::-1]


        def findMax(A,n):
            maxx = 0
            issorted=True
            for i in range(n+1):
                if A[i]>A[maxx]:
                    maxx=i
                #Check if already sorted
                if i!=0 and issorted:
                    issorted = A[i]>=A[i-1]
            return maxx if issorted==False else -1


        N= len(A)
        steps = []
        for n in range(N-1,-1,-1):
            idx= findMax(A,n)
            # Break if sorted
            if idx==-1: 
                break
            #Dont flip if in right place
            if idx != n:
                # No need to bring to idx 0
                if idx !=0:
                    reverse(A,idx)
                    steps.append(idx)
                reverse(A,n)
                steps.append(n)
        
        # Convesting into 1 based indexing
        return [i+1 for i in steps]
