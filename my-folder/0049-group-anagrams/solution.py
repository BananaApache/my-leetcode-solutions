class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        result = []
        
        for string in strs:
            key = ''.join(sorted(string))
            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)
        
        # hashmap should include keys with array of same anagrams at this state

        for key in hashmap.keys():
            result.append(hashmap[key])

        return result

