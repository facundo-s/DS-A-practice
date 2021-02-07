class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        n=[0]*n
        m=[0]*m
        for i in indices:
            n[i[0]]+=1
            m[i[1]]+=1
        n_odd=0
        
        print (n, m)
        for y in range(len(n)):
            for x in range(len(m)):
                cv=n[y]+m[x]
                if cv%2==1:
                    n_odd+=1
        return n_odd
        