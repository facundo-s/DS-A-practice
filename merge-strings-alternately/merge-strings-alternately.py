class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        l1 = len(word1)
        l2 = len(word2)
        remainder = 0
        
        if l1!=l2:
            if l1>l2:
                remainder = word1[l2:l1]
            else:
                remainder = word2[l1:l2]
                
        
        merged = [None]*(2*min(l1,l2))
        
        for i in range(min(len(word1),len(word2))):
            merged[2*i]=word1[i]
            merged[2*i+1]=word2[i] 
        
        if remainder:
            merged+=remainder

        
        return "".join(merged)
        