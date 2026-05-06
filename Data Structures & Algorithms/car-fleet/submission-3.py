class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0

        pns = []
        for i in range(0, len(position)):
            pns.append([position[i], speed[i]])
        pns = sorted(pns, reverse=True, key=lambda x: x[0])

        time_to_finish = []
        for i in pns:
            time_to_finish.append((target - i[0])/i[1])
        time_to_finish.reverse()

        fleets += 1
        curr_max = time_to_finish.pop()

        while bool(time_to_finish):
            curr = time_to_finish.pop()
            if curr_max < curr:
                fleets += 1
                curr_max = curr

        return fleets