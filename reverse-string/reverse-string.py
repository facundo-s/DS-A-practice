class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            buf = s[i]
            s[i]=s[-1+(-1)*i]
            s[-1+(-1)*i]=buf