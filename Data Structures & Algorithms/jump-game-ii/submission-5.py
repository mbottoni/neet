class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0

        while goal > 0: # Did not reach the begin
            for i in range(goal):
                if i + nums[i] >= goal: # can reach goal from the min start position
                    goal = i
                    jumps += 1
                    break
            else:
                return -1

        return jumps