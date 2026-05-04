class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tracker1 = defaultdict(int)
        tracker2 = defaultdict(int)

        for c in s:
            tracker1[c] += 1

        for c in t:
            tracker2[c] += 1

        for c in t:
            if tracker2.get(c, 0) != tracker1.get(c, 0):
                return False

        return True
        