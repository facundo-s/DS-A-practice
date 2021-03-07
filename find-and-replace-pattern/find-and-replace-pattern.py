class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        if you do list += string, it will add each character in string separately
        
        Order matters in this question, which is why my first implementation below is commented out
        
        the zip function joins the iterator elements of different data
        a = [1,2,3]
        b = ["one", "two", "three"]
        c = list(zip(a,b))
        print(c)
        >>> (1,"one"), (2,"two"), (3,"three")
        """
        def match(word):
            m1 = {}
            m2 = {}
            
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w]=p
                if p not in m2:
                    m2[p]=w
                if (m1[w],m2[p])!=(p,w):
                    return False
            return True
        return filter(match,words)
            
        
#         # extract the frequencies of each character for pattern
#         # extract frequencies of characters for each word
#         # words that have the same number of distinct frequencies are matches
        
#         matches = []
        
#         pat = [0]*26
#         for letter in pattern:
#             pat[ord(letter)-96]+=1
        
#         pat.sort()
#         for word in words:
#             character_frequency = [0]*26
#             for character in word:
#                 character_frequency[ord(character)-96]+=1
#             character_frequency.sort()
            
#             if pat == character_frequency:
#                 matches+=[word]
                
#         return matches