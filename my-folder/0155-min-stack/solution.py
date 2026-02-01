class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # dont add first element
        if len(self.stack) == 0:
            self.minStack.append(val)
            self.stack.append(val)
            return None
        
        # 2 cases
        top = self.minStack[-1]
        # if val bigger/equal to currentMin
        if val >= top:
            # map from index -> currentMin
            self.minStack.append(top)
            # add to stack
            self.stack.append(val)
        # if val smaller than currentMin
        else:
            # map from index -> new currentMin
            self.minStack.append(val)
            # add to stack
            self.stack.append(val)
    
    def pop(self) -> None:
        # assumed stack non-empty

        popped = self.stack.pop()
        top = self.minStack.pop()

        # # 2 cases
        # # if value mapped from popped index is different from currentMin
        # if self.minMap[poppedIndex] != self.currentMin:
        #     # set currentMin to that value mapped from popped index
        #     self.currentMin = self.minMap[poppedIndex]
        # # if value still same
        #     # just pop
        
        # return popped value
        return popped

    def top(self) -> int:
        # assumed stack non-empty
        # return last
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        # assumed stack non-empty
        # return currentMin
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
