class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for s in strs:
            tracker["".join(sorted(s))] = []

        for s in strs:
            if tracker.get("".join(sorted(s))) is not None:
                tracker["".join(sorted(s))].append(s)
        
        ret = []
        for k, v in tracker.items():
            ret.append(v)

        return ret