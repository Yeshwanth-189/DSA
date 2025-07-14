class Solution:
    def reorganizeString(self, s: str) -> str:
        freq_map = Counter(s)
        max_heap = [(-count, char) for char, count in freq_map.items()]
        heapq.heapify(max_heap)
        
        res = []
        prev = (0, '')

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)

            
            if prev[0] < 0:
                heapq.heappush(max_heap, prev)

        
            prev = (count + 1, char)  

        result = ''.join(res)
        return result if len(result) == len(s) else ""

            


# This code uses a max heap to rearrange characters in the string such that no two adjacent characters are the same.
# It returns the reorganized string or an empty string if it's not possible to rearrange.