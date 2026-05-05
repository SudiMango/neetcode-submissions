class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        s1_tracker = defaultdict(int)
        s2_tracker = defaultdict(int)

        for c in s1:
            s1_tracker[c] += 1

        for c in s2[0:window_len]:
            s2_tracker[c] += 1

        l = 0
        for r in range(window_len - 1, len(s2)):
            if l != 0:
                s2_tracker[s2[r]] += 1

            for i in range(l, r + 1):
                if s1_tracker.get(s2[i], 0) != s2_tracker.get(s2[i], 0):
                    break
                if i == r:
                    return True

            s2_tracker[s2[l]] -= 1
            l += 1

        return False