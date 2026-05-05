class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        curr_idx = 0
        t_idx = 0
        while curr_idx < len(s):
            curr_len = ""
            while s[t_idx] != "#":
                curr_len += s[t_idx]
                t_idx += 1
            size = int(curr_len)
            res.append(s[curr_idx + len(curr_len) + 1 : curr_idx + size + len(curr_len) + 1])
            curr_idx = curr_idx + size + len(curr_len) + 1
            t_idx = curr_idx
        return res