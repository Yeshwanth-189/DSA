class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and abs(index_map[num] - i) <= k:
                return True
            index_map[num] = i
        return False
# This code uses a dictionary to track the last index of each number.
# If a number is found again within the specified distance k, it returns True.        