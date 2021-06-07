class Solution:
    
    def minCostClimbingStairs(self, costs):
        
        expense_2, expense_1, expense_0 = 0, 0, 0 
        for i in range(2, len(costs) + 1):
            expense_0 = min(expense_2 + costs[i-2], expense_1 + costs[i-1])
            expense_1, expense_2 = expense_0, expense_1
        return expense_0
