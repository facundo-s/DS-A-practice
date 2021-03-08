class BrowserHistory:
    """
    I will attempt to optimize using a single array for history
    """
    def __init__(self, homepage: str):
        #self.homepage = homepage
        self.current = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current+1]
        self.history.append(url)
        self.current += 1
        

    def back(self, steps: int) -> str:
        if steps>self.current:
            self.current = 0
        else:
            self.current -= steps
        
        return self.history[self.current]
            

    def forward(self, steps: int) -> str:
        if steps>(len(self.history)-self.current-1):
            self.current = len(self.history)-1
        else:
            self.current += steps
        return self.history[self.current]
    
    """
    
    O(steps) back and forward
    O(1) visits
    
    

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.back_history = []
        self.current = homepage
        self.forward_history = []

    def visit(self, url: str) -> None:
        self.back_history.append(self.current)
        self.current = url
        self.forward_history=[]
        

    def back(self, steps: int) -> str:
        while steps>0:
            if len(self.back_history)==0:
                break
            self.forward_history.append(self.current)
            self.current = self.back_history.pop()
            steps-=1
        return self.current
            

    def forward(self, steps: int) -> str:
        while steps>0:
            if len(self.forward_history)==0:
                break
            self.back_history.append(self.current)
            self.current = self.forward_history.pop()
            steps-=1
        return self.current
        
    """
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)