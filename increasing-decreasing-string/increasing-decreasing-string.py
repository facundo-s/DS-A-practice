class Solution:
    def sortString(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        output = []
        s=list(s)
        count=0
        direction=True
        while s:
            if direction:
                for letter in alphabet:
                    if letter in s:
                        output+=[letter]
                        s.remove(letter)
                        count+=1
                    if count==3:
                        count=0
                        direction=False
                count=0
                direction=False
            else:
                for letter in reversed(alphabet):
                    if letter in s:
                        output+=[letter]
                        s.remove(letter)
                        count+=1
                    if count==3:
                        count=0
