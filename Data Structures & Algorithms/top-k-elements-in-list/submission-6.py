class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_hash = {}
        for i in nums:
            ct = count_hash.get(i,0)
            count_hash[i] = ct+1
        sorted_dict = dict(sorted(count_hash.items(), key=lambda item:item[1],reverse=True))

        return list(sorted_dict.keys())[:k]