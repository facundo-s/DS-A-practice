class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = [0]*len(bank)
        for i, n in enumerate(bank):
            r = 0
            #print (n)
            for j, o in enumerate(list(n)):
                #print(o)
                if o == "1":
                    r+=1      
            m[i]=r
            #print(" ")
        
        #print(m)
        result = 0
        last = 0
        for k, val in enumerate(m):
            if val != 0:
                result+=val*last
                last = val
        return result