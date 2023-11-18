class BrowserHistory:

    def __init__(self, homepage: str):

        self.curidx = 0
        self.endidx = 0
        #endidx - curidx shld show u how many steps forward u can take
        #curidx - startidx shld show u how many steps backwards
        self.history = [homepage]

    #[temp1, temp2, temp3, temp4]
    # 0, 1, 3


    def visit(self, url: str) -> None:
        print(self.curidx)
        print(self.endidx)
        while self.endidx > self.curidx:
            self.history.pop()
            self.endidx -= 1
            
        self.history.append(url)
        self.endidx = self.curidx + 1
        self.curidx += 1
      
        

    def back(self, steps: int) -> str:

        canmoveback = self.curidx - 0
        shouldmoveback = min(canmoveback,steps)

        self.curidx = self.curidx - shouldmoveback
        return self.history[self.curidx]
        

    def forward(self, steps: int) -> str:

        canmoveforward = self.endidx - self.curidx

        shouldmoveforward = 0
        shouldmoveforward = min(canmoveforward,steps)

        self.curidx = self.curidx + shouldmoveforward

        return self.history[self.curidx]
        



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)