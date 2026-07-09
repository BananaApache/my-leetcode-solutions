class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total = 0
        differences = []

        for index in range(len(gas)):
            differences.append(gas[index] - cost[index])
            total += differences[index]
        
        if total < 0:
            return -1
        
        runningTotal = 0
        result = 0

        for start in range(len(differences)):
            runningTotal += differences[start]
            if runningTotal < 0:
                runningTotal = 0
                result = start + 1
        
        return result
            

