class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res  = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

        res = dict(sorted(res.items(), key=lambda item: item[1], reverse = True))
        
        vals = list(res.keys())

        return vals[:k]