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
        
# This code uses a two-pointer technique to find the maximum area of water that can be contained between two lines in a list of heights.
# The pointers start at the beginning and end of the list and move towards each other, calculating the area at each step.