class Solution:
    dynamic = [[]]
    def simplifiedFractions(self, n: int) -> List[str]:
        # go down n until you get to 1
        # for each n generate all possible fractions, discard the reducible ones
        # the reducible ones are the ones that gcf lcm. If gcf==1, don't save
        # this fits a dynamic programming solution
        
        # in this exercise I learned that I can use math.gcd() to get the gcd
#         if n==0:
#             return []
#         fractions = []
#         for i in range(1,n):
#             if math.gcd(i,n)==1:
#                 fractions += [str(i)+"/"+str(n)]
                
#         return fractions + self.simplifiedFractions(n-1)


        if len(Solution.dynamic)>n:
            fractions = []
            for i_n in range(0,n):
                fractions+=Solution.dynamic[i_n]
            return fractions
        else:
            fractions = []
            for i_n in range(0,len(Solution.dynamic)):
                fractions+=Solution.dynamic[i_n]
            for i_n in range(len(Solution.dynamic),n+1):
                current = []
                for i in range(1, i_n):
                    if math.gcd(i, i_n)==1:
                        current.append(str(i)+"/"+str(i_n))
                Solution.dynamic.append(current)
                fractions+=current
            return fractions
    
    