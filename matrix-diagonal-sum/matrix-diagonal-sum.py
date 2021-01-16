class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i=0
        j1=0
        j2=len(mat)-1
        total=0
        while i<len(mat):
            if j1==j2:
                total+=mat[i][j1]
            else:
                total+=mat[i][j1]+mat[i][j2]
            j1+=1
            j2-=1
            i+=1
        return total
