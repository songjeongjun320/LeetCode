from typing import List, Tuple

class RecentCounter:
    def __init__(self):
        self.request = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.request.append(t)
        for i in range(self.start, len(self.request)):
            if self.request[i] < t - 3000:
                self.start += 1
        return len(self.request) - self.start

sol: RecentCounter = RecentCounter()
param_1:int = sol.ping(1)
print(param_1)
param_1:int = sol.ping(100)
print(param_1)
param_1:int = sol.ping(3001)
print(param_1)
param_1:int = sol.ping(3002)
print(param_1)
