class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack1 = []
        stack2 = []
        res = []

        active_temp = temperatures.pop()
        stack1.append(active_temp)
        res.append(0)

        disp = 1
        while bool(temperatures):
            active_temp = temperatures.pop()

            if bool(stack1) and stack1[-1] > active_temp:
                res.append(disp)
                disp = 1
                stack1.append(active_temp)
                continue

            while bool(stack1) and stack1[-1] <= active_temp:
                stack2.append(stack1.pop())
                disp += 1

            if not bool(stack1):
                res.append(0)
                disp = 1
                while bool(stack2):
                    stack1.append(stack2.pop())
                stack1.append(active_temp)
            else:
                if stack1[-1] > active_temp:
                    res.append(disp)
                    disp = 1
                    while bool(stack2):
                        stack1.append(stack2.pop())
                    stack1.append(active_temp)

        res.reverse()
        return res