class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        popcount=0
        if(not self.stack or self.stack[-1][0]>price):
            self.stack.append( (price,0) ) # price,0  indicates that popcount for this is 0
            return 1
        
        while(self.stack and price>=self.stack[-1][0]):
            popcount+= self.stack.pop()[1]+1 # all ele that were popped for pushing this ele + 1(for popping this ele)
            
        self.stack.append( (price,popcount) ) # push total popcount for cur price
         
        return popcount+1
