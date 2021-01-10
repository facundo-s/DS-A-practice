class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches=0
        while n>1:
            if n%2==0:
                #even
                n=n/2
                matches+=n
            else:
                n=n/2
                matches+=n
                n+=1
        return matches
        
