class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total=numBottles
        while numBottles>=numExchange:
            numBottles=numBottles-numExchange+1
            total+=1
        return total
            
