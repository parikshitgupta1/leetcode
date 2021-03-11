class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        minCount = [MAX] * (amount + 1)
        minCount[0] = 0

        for current in range(1, amount + 1, 1):
            for value in coins:
                if value > current:
                    continue
                
                minCount[current] = min(minCount[current - value] + 1, minCount[current])

        return minCount[amount] if minCount[amount] != MAX else -1
