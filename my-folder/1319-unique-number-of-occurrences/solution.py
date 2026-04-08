class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        from collections import Counter
        hashmap = Counter(arr)
        return len(hashmap.values()) == len(set(list(hashmap.values())))

