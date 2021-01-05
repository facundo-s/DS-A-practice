class OrderedStream(object):
​
    def __init__(self, n):
        """
        :type n: int
        """
        self.ptr = 0
        self.stream_list = [None]*n
        
​
    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        id=id-1
        self.stream_list[id] = value
        if id==self.ptr:
            return_list = []
            while self.stream_list[self.ptr]!=None:
                return_list+=[self.stream_list[self.ptr]]
                self.ptr+=1
                if self.ptr==len(self.stream_list):
                    break
            return return_list
        else:
            return []
        
​
​
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
