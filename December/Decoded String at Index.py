class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        corresponding_length = [1]
        for i in S[1:]:
            if corresponding_length[-1] >= K:
                break
            if i.isdigit():
                corresponding_length.append(corresponding_length[-1] * int(i))
            else:
                corresponding_length.append(corresponding_length[-1] + 1)
        
        print(corresponding_length)
        end = len(corresponding_length) - 1
        while corresponding_length[end] > K:
            end -= 1
            if corresponding_length[end] < K:
                #K = ((K-1) % corresponding_length[end]) + 1 
                K = K % corresponding_length[end]
                if K == 0:
                    K = corresponding_length[end]
        while S[end].isdigit():
            end -= 1
        return S[end]   
