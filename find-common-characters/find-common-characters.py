class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        frequency_dict = [None]*len(A)
        for i, l in enumerate(A):
            f_d = [0]*26
            for c in l:
                f_d[ord(c)-97]+=1
            frequency_dict[i]=f_d
        output = []
        for i in range(0,26):
            min_freq = min(map(lambda x: x[i], frequency_dict))
            output+=[chr(i+97)]*min_freq
            
        return output
            