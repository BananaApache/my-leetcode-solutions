class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        priceTo = [ float("inf") ] * n
        priceTo[src] = 0
        
        for _ in range(k + 1):
            tmp = priceTo.copy()

            for start, end, price in flights:
                if priceTo[start] + price < tmp[end]:
                    tmp[end] = priceTo[start] + price

            priceTo = tmp
        
        if priceTo[dst] == float("inf"):
            return -1
        else:
            return priceTo[dst]

