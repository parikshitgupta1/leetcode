class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 1 and gas[0] >= cost[0]:
            return 0
            
        for i in range(n):
            if gas[i] < cost[i]:
                continue
            else:
                start_idx = i
                end_idx = (i + 1) % n
                j = i
                cost_ = gas[j]
                while start_idx != end_idx:
                    cost_ =  cost_ - cost[j] + gas[end_idx]
                    if cost_ < cost[end_idx]:
                        break
                    else:
                        end_idx = (end_idx+1)%n
                        j = (j+1) % n
                        if start_idx == end_idx:
                            return start_idx
        return -1
