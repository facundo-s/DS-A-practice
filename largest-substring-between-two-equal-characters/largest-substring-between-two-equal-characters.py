class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        character_dict={}
        for i in range(len(s)):
            if s[i] in character_dict: 
                character_dict[s[i]].append(i)
            else:
                character_dict[s[i]]=[i]
        
        max_so_far = -1
        for letter in character_dict.keys():
            if len(character_dict[letter])==1:
                continue
            else:
                current_length = max(character_dict[letter])-min(character_dict[letter])-1
                if current_length>max_so_far:
                    max_so_far=current_length
        
        return max_so_far
        
