class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i in d:
                d[i] += 1  # Fixed indentation
            else:
                d[i] = 1   # Fixed initial count from 0 to 1
        
        lista = sorted(d, key=d.get, reverse=True)
        
        l = lista[:k]
        
        return l