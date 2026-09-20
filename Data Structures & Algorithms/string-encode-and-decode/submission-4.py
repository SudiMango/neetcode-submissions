class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for s in strs:
            ret += str(len(s))
            ret += "#"
            ret += s

        return ret

    def decode(self, s: str) -> List[str]:
        ret = []

        started = False
        counter = 0
        curr_str = ""
        str_len_str = ""
        str_len = -1

        for i, c in enumerate(s):
            if not started:
                if c == "#":
                    str_len = int(str_len_str)
                    if str_len == 0:
                        ret.append("")
                        curr_str = ""
                        counter = 0
                        str_len_str = ""
                        str_len = -1
                    else:
                        started = True
                else:
                    str_len_str += c
                
                continue

            curr_str += c
            counter += 1
            if counter == str_len:
                ret.append(curr_str)
                curr_str = ""
                counter = 0
                str_len_str = ""
                str_len = -1
                started = False

        return ret