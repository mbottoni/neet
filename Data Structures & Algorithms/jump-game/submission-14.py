class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            # Can the current reach the goal?
            # If yes we mark the current as True and update goal to current?
            print(i)
            steps = nums[i]
            if i + steps >= goal:
                goal = i

        if goal==0:
            return True
        return False