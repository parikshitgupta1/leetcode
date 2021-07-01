class Solution:
    def grayCode(self, n: int) -> List[int]:
        answer = list()
        for i in range(2**n):
            answer.append(i ^ (i//2))  # XOR based solution
        return answer
