class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet=list("@abcdefghijklmnopqrstuvwxyz")
        letters = []
        s=list(s)
        while s:
            if s[-1]=="#":
                this_letter = alphabet[int("".join(s[-3:-1]))]
                s.pop(-1)
                s.pop(-1)
                s.pop(-1)
            else:
                this_letter=alphabet[int(s[-1])]
                s.pop(-1)
            letters.append(this_letter)
        return "".join(reversed(letters))
            
            