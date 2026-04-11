class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost)>sum(gas):
            return -1
        total = 0
        result = 0
        for i in range(n):
            diff   = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                result = i + 1

        return result

        