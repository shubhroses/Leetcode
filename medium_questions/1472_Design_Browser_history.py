class BrowserHistory:

    def __init__(self, homepage: str):
        self.saved = [homepage]
        self.cur = 0
        
    def visit(self, url: str) -> None:
        self.saved = self.saved[:self.cur+1] + [url]
        self.cur += 1

    def back(self, steps: int) -> str:
        moveback = min(steps, self.cur)
        self.cur -= moveback
        return self.saved[self.cur]

    def forward(self, steps: int) -> str:
        moveforward = min(len(self.saved)-1-self.cur, steps)
        self.cur += moveforward
        return self.saved[self.cur]
        
"""


["homepage", "Google"] list with a pointer in list
     cur
     
 moveforward = min()
cur = 0
len(saved) = 2

back = 1


"""

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)