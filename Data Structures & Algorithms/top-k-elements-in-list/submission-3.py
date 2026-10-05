class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 0
            res[i] += 1
        
        sorted_dict = list(sorted(res.items(),key=lambda item: item[1],reverse=True))
        a = []
        for i in sorted_dict[:k]:
            a.append(i[0])
        
        return a