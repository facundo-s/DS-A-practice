class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s=list(s)
        r=[None]*len(s)
        for i in range(len(indices)):
            r[indices[i]]=s[i]
        return "".join(r)
