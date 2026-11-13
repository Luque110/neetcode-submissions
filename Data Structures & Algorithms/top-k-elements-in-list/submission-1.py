class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        l = []
        for i in nums:
            if i in d:
               d[i]+=1
            else:
                d[i] = 0
        
        lista = sorted(d, key=d.get, reverse=True)
        
        l = lista[:k]
        
        return l
         
