class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer_list = []

        max_candies = max(candies)

        for kids_candy in candies:
            if kids_candy + extraCandies >= max_candies:
                answer_list.append(True)
            else:
                answer_list.append(False)

        return answer_list
        
