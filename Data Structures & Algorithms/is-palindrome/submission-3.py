class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        print(lower)
        cleaned = re.sub("[^a-z0-9]", "", lower)
        print(cleaned)

        l = 0
        r = len(cleaned) - 1

        while l <= r:
            if cleaned[l] == cleaned[r]:
                l += 1
                r -= 1
            else:
                return False

        return True