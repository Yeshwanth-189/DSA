class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p_m=m-1
        p_n=n-1
        p=m+n-1
        while p_m>=0 and p_n>=0:
            if nums1[p_m]>nums2[p_n]:
                nums1[p]=nums1[p_m]
                p_m-=1
            else:
                nums1[p]=nums2[p_n]
                p_n-=1
            p-=1
        while p_n>=0:
            nums1[p]=nums2[p_n]
            p_n-=1
            p-=1
        

# It uses two pointers to track the current position in each array and fills nums1 from the end to avoid overwriting elements.
# The while loops ensure that all elements from both arrays are considered, and any remaining elements in nums2 are copied over if necessary.
