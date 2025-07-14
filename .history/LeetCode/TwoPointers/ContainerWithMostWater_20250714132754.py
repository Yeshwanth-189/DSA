class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_water=float("-inf")
        while i<j:
            min_height=min(height[i],height[j])
            water=min_height*(j-i)
            if water>max_water:
                max_water=water
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max_water