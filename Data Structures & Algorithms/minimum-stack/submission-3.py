class MinStack:
    def __init__(self):
        self.stack = []
        self.min_current = math.inf

    def push(self, val: int) -> None:
        self.stack.append([val,self.min_current]) 

        if (val<self.min_current): 
            self.min_current = val
         

    def pop(self) -> None:
        if self.top() == self.min_current:
            self.min_current = self.stack[-1][1]

        self.stack.pop() 

        
    def top(self) -> int:
        return self.stack[-1][0] 

    def getMin(self) -> int:
        return self.min_current 


