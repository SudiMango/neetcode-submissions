class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        max_len = 0
        curr_len = 0

        l = 0
        r = 0

        char_to_count = defaultdict(int)
        char_to_count[s[l]] += 1

        while True:
            if r == len(s):
                return max_len + 1

            if l == r:
                if r + 1 == len(s):
                    return max_len + 1
                else:
                    r += 1
                    char_to_count[s[r]] += 1
            
            if char_to_count.get(s[r], 0) > 1:
                char_to_count[s[l]] -= 1
                l += 1
            else:
                curr_len = r - l
                if curr_len > max_len:
                    max_len = curr_len
                r += 1
                if r < len(s):
                    char_to_count[s[r]] += 1

            

            
            