class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        own_stock=False
        profit=0
        
        for i in range(len(prices)):
            if not own_stock:
                if i==len(prices)-1:
                    continue
                if prices[i]<prices[i+1]:
                    #buy
                    buy_price = prices[i]
                    own_stock=True
                continue
            else:
                if i==len(prices)-1:
                    #if you reached the end and you still own you should sell
                    profit+=prices[i]-buy_price
                    own_stock=False
                    continue
                if prices[i]>prices[i+1]:
                    #sell
                    profit+=prices[i]-buy_price
                    own_stock=False
                continue
        return profit
                
            
        
        #buy = -1
        #sell = -1
        #total_sum=0
        #for i in range(len(prices)):
        #    inverted_index = len(prices)-i
        #    if sell<0 or prices[i]>prices[sell]:
        #        sell=i
            
