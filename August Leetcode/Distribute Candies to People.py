class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = [0 for i in range(num_people)]
        index = 0
        while candies>0:
            n[index%num_people]+= min(candies,index+1)
            candies-=index+1
            index+=1
        return n
