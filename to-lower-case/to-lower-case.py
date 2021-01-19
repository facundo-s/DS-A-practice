class Solution:
    def toLowerCase(self, str: str) -> str:
        rl=[]
        for n in str:
            asc=ord(n)
            if asc>=65 and asc<=65+26: #and asc<97:
                rl.append(chr(asc+32))
            else:
                rl.append(n)
        return "".join(rl)
