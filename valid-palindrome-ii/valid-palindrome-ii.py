class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        i=0
        j=len(s)-1
        
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            else:
                break
        
        if i==j:
            return True
        
        # at this point you exit the while loop with i and j identifying
        # where the item to be removed is
        # the two cases are either remove the element at i or at j, and check for palyndrome
        
        #case one
        one = s[:i]+s[i+1:]
        result_one = one == one[::-1]
        
        #case two
        two = s[:j]+s[j+1:]
        result_two = two == two[::-1]
            
        return result_one or result_two
