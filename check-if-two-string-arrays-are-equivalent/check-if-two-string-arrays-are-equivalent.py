class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        str1=""
        for l in word1:
            str1+=l
        
        str2=""
        for l in word2:
            str2+=l
            
        return str1==str2
        
