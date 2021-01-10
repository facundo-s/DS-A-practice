class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        #richest_customer=0
        max_wealth=0
        
        for i in range(len(accounts)):
            #for all the customers
            current_wealth=0
            for j in range(len(accounts[i])):
                # for all their accounts add their money
                current_wealth+=accounts[i][j]
            if current_wealth>max_wealth:
                max_wealth=current_wealth
                #richest_customer=i
            
        return max_wealth
​
        
