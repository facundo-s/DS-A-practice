class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set()
        for letter in allowed:
            allowed_set.add(letter)
        
        count = 0
        for word in words:
            passed = True
            for letter in word:
                if letter not in allowed_set:
                    passed = False
                    break
            if passed:
                count+=1
        
        return count
