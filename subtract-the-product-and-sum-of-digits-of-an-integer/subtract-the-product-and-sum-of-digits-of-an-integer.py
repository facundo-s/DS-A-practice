class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
#         sum_n=0
#         prod_n=1
#         for digit in str(n):
#             sum_n+=int(digit)
#             prod_n*=int(digit)
            
#         return prod_n-sum_n
        sum_n = 0 
        prod_n = 1
        while n>0:
            digit = n%10
            sum_n+=digit
            prod_n*=digit
            n=n//10
        return prod_n-sum_n
        
