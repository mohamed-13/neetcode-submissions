class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lib = {}

        for i in strs:
            sorted_i = sorted(i)
            sorted_i = "".join(sorted_i)
            if sorted_i not in lib:
                lib[sorted_i] = [i]
            else:
                lib[sorted_i].append(i)

        res=[]
        for i in lib:
            res.append(lib[i])

        return res