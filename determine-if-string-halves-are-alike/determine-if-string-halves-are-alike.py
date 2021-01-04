class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = 0
        i = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i<len(s)/2:
            if s[i] in vowels:
                a+=1
            if s[len(s)/2+i] in vowels:
                b+=1
            i+=1
        
        return a==b
        
