class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        anagram = {}
        
        # add all characters of s to a dictionary
        for character in s:
            if character in anagram:
                anagram[character]+=1
            else:
                anagram[character]=1
        
        steps=0
        for character in t:
            if character in anagram:
                if anagram[character]==0:
                    steps+=1
                else:
                    anagram[character]-=1
            else:
                steps+=1
        
        return steps
                
                    
        
