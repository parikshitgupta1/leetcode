class Solution:
    def threeEqualParts(self, A):
        print(A.count(1)+A.count(0))
        ones = A.count(1)
        i, j, k, x, y, A_len = 0, 0, 0, -1, -1, len(A)
        if not ones:
            return [0, A_len - 1]
        if ones%3 != 0:
            return [x, y]
        
        step1, step2 = ones//3+1, ones*2//3+1

        for p, num in enumerate(A):
            if num == 1:
                i = p
                break

        for p, num in enumerate(A):
            if num == 1:
                step1 -= 1
            if 0 == step1:
                j = p
                break

        for p, num in enumerate(A):
            if num == 1:
                step2 -= 1
            if 0 == step2:
                k = p
                break

        while k < A_len and A[i] == A[j] and A[j] == A[k]:
            i += 1
            j += 1
            k += 1

        if k == A_len:
            return [i-1,j]

        return [-1,-1]
