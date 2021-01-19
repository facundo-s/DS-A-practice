class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B=[]
        for i, row in enumerate(A):
            new_row=[]
            for i in reversed(row):
                new_row.append(i^1)
            B.append(new_row)
        return B
