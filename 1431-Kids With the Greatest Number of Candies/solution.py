class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        output: list[bool] = []
        max_candy: int = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                output.append(True)
            else:
                output.append(False)
        return output

solution = Solution()
candies:list[int] = [2,3,5,1,3]
extraCandies:int = 3
print(solution.kidsWithCandies(candies, extraCandies))