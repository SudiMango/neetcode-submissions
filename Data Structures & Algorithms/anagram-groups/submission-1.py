class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_item = defaultdict(list)
        ret = []

        for s in strs:
            s_sorted = "".join(sorted(s))
            sorted_to_item[s_sorted].append(s)
        
        for k, v in sorted_to_item.items():
            ret.append(v)

        return ret